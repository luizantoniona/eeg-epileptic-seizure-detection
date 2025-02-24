import numpy as np
import mne
import re
import Object.Signal.SignalFactory as SignalFactory
from Object.Signal.Signal import Signal
from Object.Signal.SignalTypeEnum import SignalTypeEnum
import Reader.ReaderCommons as Commons


class Summary:
    """
    A class representing a summary of data.

    Attributes:
    - dataset_name (str): Name of the dataset.
    - record_name (str): Name of the record.
    - file_name (str): Name of the data file.
    - start_time (str): Start time of the data.
    - end_time (str): End time of the data.
    - nr_occurrence (int): Number of occurrence of the disease in the data.
    - start_occurrence (list): List of start times of disease occurrence.
    - end_occurrence (list): List of end times of disease occurrence.
    - nr_channels (int): Number of data channels.
    - ds_channels (list): List of data channels.
    - disease_type (str): Type of the disease.
    - signal: An instance of signal model (Signal).
    """

    def __init__(self, dataset_name: str, record_name: str, file_name: str, start_time, end_time, nr_occurrence: int, start_occurrence, end_occurrence, nr_channels, ds_channels, disease_type: str):

        self.dataset_name = dataset_name
        self.record_name = record_name
        self.file_name = file_name
        self.start_time = start_time
        self.end_time = end_time
        self.nr_occurrence = nr_occurrence
        self.start_occurrence = start_occurrence
        self.end_occurrence = end_occurrence
        self.nr_channels = nr_channels
        self.ds_channels = ds_channels
        self.disease_type = disease_type
        self.signal: Signal

    def __str__(self):
        return f"{self.record_name}:({self.file_name})"

    def fullpath(self):
        """
        Return the full path of the data file.
        """
        return "./data/" + self.dataset_name + "/" + self.record_name + "/" + self.file_name

    def get_nr_occurrence(self):
        return self.nr_occurrence

    def duration(self):
        """
        Return the duration of the data in seconds.
        """
        duration = self.end_time - self.start_time
        return duration.total_seconds()

    def start_time_of_ocurrence(self, nr_seizure=0):
        """
        Return the start time of a specific seizure.
        """
        if nr_seizure > self.nr_occurrence:
            return 0
        else:
            return self.start_occurrence[nr_seizure - 1]

    def end_time_of_ocurrence(self, nr_seizure=0):
        """
        Return the end time of a specific seizure.
        """
        if nr_seizure > self.nr_occurrence:
            return 0
        else:
            return self.end_occurrence[nr_seizure - 1]

    def has_anomaly_in_interval(self, tmin, tmax) -> str:
        """
        Check if there are anomaly in time interval.
        """
        has_anomaly = "normal"

        for i in range(self.nr_occurrence):
            if self.start_time_of_ocurrence(i) <= tmin < self.end_time_of_ocurrence(i) or self.start_time_of_ocurrence(i) < tmax <= self.end_time_of_ocurrence(i):
                has_anomaly = self.disease_type

        return has_anomaly

    def generate_segmented_data_full_file(self, signal_type: SignalTypeEnum, window_length: int, overlap_shift_size: int):
        """
        Generate segmented data based on type and a specified time window for full file.
        """
        self.signal: Signal = SignalFactory.signal_by_type(signal_type, self.read_edf())

        current_time = 0
        while current_time + window_length <= self.duration():
            self.signal.generate_segmented_data(current_time, current_time + window_length)
            self.signal.label_segmented.append(self.has_anomaly_in_interval(current_time, current_time + window_length))
            current_time += overlap_shift_size

        self.signal.delete_mne_data()

    def generate_segmented_data_around_seizures(self, signal_type: SignalTypeEnum, window_length: int, overlap_shift_size: int):
        """
        Generate segmented data based on type and a specified time window around disease ocurrence.
        """
        self.signal = SignalFactory.signal_by_type(signal_type, self.read_edf())

        for ocurrence_index in range(self.nr_occurrence):

            start_occurrence_time = self.start_occurrence[ocurrence_index]
            end_occurrence_time = self.end_occurrence[ocurrence_index]
            seizure_duration = end_occurrence_time - start_occurrence_time

            fragment_start = start_occurrence_time - int(seizure_duration / 2)
            fragment_end = end_occurrence_time + int(seizure_duration / 2)

            if fragment_start <= 0:
                fragment_start = 0

            if fragment_end > self.duration():
                fragment_end = self.duration()

            current_time = fragment_start

            while current_time + window_length <= fragment_end:
                self.signal.generate_segmented_data(current_time, current_time + window_length)
                self.signal.label_segmented.append(self.has_anomaly_in_interval(current_time, current_time + window_length))
                current_time += overlap_shift_size

        self.signal.data_segmented = np.array(self.signal.data_segmented) if self.signal.data_segmented else None
        self.signal.label_segmented = np.array(self.signal.label_segmented) if self.signal.label_segmented else None
        self.signal.delete_mne_data()

    def read_edf(self, rename=False):
        mne_model = mne.io.read_raw_edf(self.fullpath(), include=Commons.selected_channels(), preload=False, verbose="critical")

        mne_model.drop_channels(Commons.remove_channels(), on_missing="ignore")

        if "T8-P8-0" in mne_model.info["ch_names"]:
            mne_model.rename_channels(Commons.rename_channels())

        mne_model.reorder_channels(Commons.selected_channels())

        if self.nr_occurrence > 0:
            start_times = []
            duration = []
            event_name = []

            for ocurrence_index in range(self.nr_occurrence):
                start_times.append(self.start_occurrence[ocurrence_index])
                duration.append(self.end_occurrence[ocurrence_index] - self.start_occurrence[ocurrence_index])
                event_name.append("Anomaly - " + str(ocurrence_index))

            mne_model.set_annotations(mne.Annotations(np.array(start_times), np.array(duration), np.array(event_name)))
            if rename:
                self.rename_channels(mne_model)

        return mne_model

    def rename_channels(self, mne_object: mne.io.BaseRaw):
        replace_dict = {}
        drop_list = []
        for channel_name in mne_object.info["ch_names"]:
            name_change = re.findall("\\w+", channel_name)[0].title()
            if name_change in list(replace_dict.values()):
                drop_list.append(channel_name)
            else:
                replace_dict[channel_name] = name_change

        mne_object.drop_channels(drop_list)
        mne_object.rename_channels(replace_dict)
        mne_object.set_montage("standard_1020")
