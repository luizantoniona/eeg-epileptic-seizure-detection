import mne

class SignalModel:
    """
    A class representing an MNE signal model.

    Attributes:
    - time_data (mne.io.Raw): MNE raw data object.
    - freq_data (mne.time_frequency.Spectrum): MNE Spectrum data object after computing power spectral density (PSD).
    - time_segments (list): List to store time segmented data.
    - freq_segments (list): List to store frequency segmented data.
    - label_segments (list): List to store labels about data segments.
    """

    def __init__(self, mne_object: mne.io.Raw):
        self.time_data = mne_object
        self.freq_data: mne.time_frequency.Spectrum = None
        self.time_segments = []
        self.freq_segments = []
        self.label_segments = []

    def generate_freq_data(self):
        self.freq_data = self.time_data.copy().compute_psd(verbose=False)

    def get_time_data(self):
        """
        Get the time-domain data.
        """
        return self.time_data.get_data()

    def get_time_segmented_data(self):
        """
        Get the time segmented data.
        """
        return self.time_segments

    def get_freq_data(self):
        """
        Get the frequency-domain data.
        """
        return self.freq_data.get_data()

    def get_freq_segmented_data(self):
        """
        Get the frequency segmented data.
        """
        return self.freq_segments
    
    def get_label_segments(self):
        """
        Get the labels of each segment.
        """
        return self.label_segments

    def sampling_freq(self):
        """
        Get the sampling frequency of the data.
        """
        return self.time_data.info["sfreq"]

    def get_frequencies(self):
        """
        Get frequencies values for freq domain data.
        """
        return self.freq_data.get_data(return_freqs=True)[1]

    def info(self):
        """
        Get the info of the data.
        """
        return self.time_data.info

    def segment_time_data_by_interval(self, t_min, t_max):
        """
        Segment time data for a specified time interval.
        """
        self.time_segments.append(self.time_data.get_data(tmin=t_min, tmax=t_max))

    def segment_freq_data_by_interval(self, t_min, t_max):
        """
        Segment frequency data for a specified time interval.
        """
        self.freq_segments.append(self.time_data.compute_psd(tmin=t_min, tmax=t_max).get_data())

    def del_time_data(self):
        """
        Delete time_data from memory.
        """
        del self.time_data
