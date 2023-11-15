import mne
from scipy.signal import spectrogram
class MNESignalModel:
    def __init__(self, mne_object: mne.io.Raw):
        self.time_data = mne_object
        self.freq_data = mne_object.copy().compute_psd()
        self.time_freq_data = []

        for buffer in mne_object.get_data():
            freq, time, Sxx = spectrogram(buffer, fs=mne_object.info['sfreq'])
            self.time_freq_data.append((freq, time, Sxx))

    def get_time_data(self):
        return self.time_data.get_data(return_times=True)
    
    def get_freq_data(self):
        return self.freq_data.get_data(return_freqs=True)
    
    def get_time_fre_data(self):
        return self.time_freq_data

    def sampling_freq(self):
        return self.time_data.info['sfreq']