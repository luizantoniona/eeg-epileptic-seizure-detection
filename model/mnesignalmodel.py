import mne
from scipy.signal import spectrogram
class MNESignalModel:
    def __init__(self, mne_object: mne.io.Raw):
        self.time_data = mne_object
        self.freq_data = mne_object.copy().compute_psd()
        self.time_freq_data = []

        for buffer in mne_object.get_data():
            f, t, Sxx = spectrogram(buffer, fs=mne_object.info['sfreq'])
            self.time_freq_data.append((f, t, Sxx))