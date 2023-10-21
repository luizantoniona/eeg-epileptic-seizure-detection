import reader.mnereader as mnereader
import reader.rawreader as rawreader
import model.signalmodel as signalmodel
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

    def __init__(self, record_name, file_name, start_time, end_time, nr_seizures, start_seizure, end_seizure, nr_channels, ds_channels):
        self.record_name = record_name
        self.file_name = file_name
        self.start_time = start_time
        self.end_time = end_time
        self.nr_seizures = nr_seizures
        self.start_seizure = start_seizure
        self.end_seizure = end_seizure
        self.nr_channels = nr_channels
        self.ds_channels = ds_channels

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
        
    def compute_mne_objects(self, rename = False):
        mne_object = mnereader.mne_edf(self, rename)
            
        self.time_data = mne_object
        self.psd_data = mne_object.copy().compute_psd()
        self.spec_data = "" #TODO: Calcular Espectro de Potência com o MNE

    def compute_all_raw(self):
        channels_names, channels_frequencies, channels_buffers = rawreader.raw_edf(self)
        self.signal = signalmodel.SignalModel(channels_names, channels_frequencies, channels_buffers)