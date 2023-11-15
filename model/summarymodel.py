import reader.mnereader as mnereader
import reader.reader as reader
import model.rawsignalmodel as rawsignal
import model.mnesignalmodel as mnesignal
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
    signal = None

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
        """Return the full path of the data file."""
        return "./data/" + self.record_name + "/" + self.file_name
    
    def duration(self):
        """Return the duration of the data in seconds."""
        duration = self.end_time - self.start_time
        return duration.total_seconds()
    
    def start_time_of_seizure(self, nr_seizure = 0):
        """Return the start time of a specific seizure."""
        if nr_seizure > self.nr_seizures:
            return 0
        else:
            return self.start_seizure[nr_seizure - 1]
        
    def end_time_of_seizure(self, nr_seizure = 0):
        """Return the end time of a specific seizure."""
        if nr_seizure > self.nr_seizures:
            return 0
        else:
            return self.end_seizure[nr_seizure - 1]
        
    def has_anomaly(self) -> bool:
        """Check if there are seizures."""
        return self.nr_seizures > 0
        
    def generate_mne(self, rename = False) -> None:
        """Generate an MNE signal model."""
        self.signal =  mnesignal.MNESignalModel( mnereader.mne_edf(self, rename) )

    def generate_signal(self) -> None:
        """Generate a raw signal model."""
        self.signal = rawsignal.RawSignalModel( *reader.edf(self) )
