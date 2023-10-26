import mne
import numpy as np
import reader.mnereader as mnereader
class SummaryModel:
    record_name = ""
    file_name = ""
    start_time = ""
    end_time = ""
    nr_seizures = 0
    start_seizure = []
    end_seizure = []
    nr_channels = 0
    ds_channels = []
    signal: mne.io.Raw
    psd: mne.time_frequency.Spectrum
    spectogram: mne.time_frequency.EpochsTFR

    def __init__(self, record_name, file_name, start_time, end_time, nr_seizures, start_seizure, end_seizure, nr_channels, ds_channels, rename):
        self.record_name = record_name
        self.file_name = file_name
        self.start_time = start_time
        self.end_time = end_time
        self.nr_seizures = nr_seizures
        self.start_seizure = start_seizure
        self.end_seizure = end_seizure
        self.nr_channels = nr_channels
        self.ds_channels = ds_channels
        self.signal = mnereader.mne_edf(self, rename)

    def __str__(self):
        return f"{self.record_name}:({self.file_name})"
    
    def fullpath(self):
        return "./data/" + self.record_name + "/" + self.file_name
    
    def duration(self):
        duration = self.end_time - self.start_time
        return duration.total_seconds()
    
    def start_time_of_seizure(self, nr_seizure = 0):
        if nr_seizure > self.nr_seizures:
            return 0
        else:
            return self.start_seizure[nr_seizure - 1]
        
    def end_time_of_seizure(self, nr_seizure = 0):
        if nr_seizure > self.nr_seizures:
            return 0
        else:
            return self.end_seizure[nr_seizure - 1]

    def generate_psd(self, method='welch'):
        self.psd = self.signal.copy().compute_psd(method)

    def generate_spectogram(self):
        frequencies = np.arange(1, int(self.signal.info['sfreq']/2), 1)
        n_cycles = frequencies / 2
        # self.spectogram = mne.time_frequency.tfr_multitaper( mnereader.mne_epochs(self),
        #                                                      frequencies,
        #                                                      n_cycles,
        #                                                      return_itc=False )
