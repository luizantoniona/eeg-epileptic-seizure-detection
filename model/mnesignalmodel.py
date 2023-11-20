import mne
from scipy.signal import spectrogram
class MNESignalModel:

    """
    A class representing an MNE signal model.

    Attributes:
    - time_data (mne.io.Raw): MNE raw data object.
    - freq_data (mne.io.Raw): MNE raw data object after computing power spectral density (PSD).
    - time_freq_data (list): List of tuples containing frequency, time, and spectrogram for each data buffer.
    - segments (list): List to store segmented data.

    """

    def __init__(self, mne_object: mne.io.Raw):
        self.time_data = mne_object
        self.freq_data = mne_object.copy().compute_psd()
        self.time_freq_data = []
        self.segments = []

        for buffer in mne_object.get_data():
            freq, time, Sxx = spectrogram(buffer, fs=mne_object.info['sfreq'])
            self.time_freq_data.append((freq, time, Sxx))

    def get_time_data(self):
        """Get the time-domain data."""
        return self.time_data.get_data(return_times=True)
    
    def get_freq_data(self):
        """Get the frequency-domain data."""
        return self.freq_data.get_data(return_freqs=True)
    
    def get_time_fre_data(self):
        """Get the time-frequency data."""
        return self.time_freq_data
    
    def get_segmented_data(self):
        """Get the segmented data."""
        return self.segments
    
    def sampling_freq(self):
        """Get the sampling frequency of the data."""
        return self.time_data.info['sfreq']
    
