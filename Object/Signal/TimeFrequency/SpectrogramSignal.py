from Object.Signal.Signal import Signal
import mne
import numpy as np

class SpectrogramSignal(Signal):
    """
    A class representing a Spectrogram signal model.
    """

    def __init__(self, mne_object: mne.io.Raw):
        super().__init__(mne_object)

    def generate_data(self):
        """
        Generate Spectogram data for all file.
        """
        self.data = self.mne_data.compute_tfr(method='morlet',
                                                     freqs=self.frequencies(),
                                                     n_jobs=-1,
                                                     verbose='CRITICAL',
                                                     n_cycles=self.frequencies()).get_data()

    def generate_segmented_data(self, t_min, t_max):
        """
        Generate segmented Spectogram data for a specified time interval.
        """
        self.data_segmented.append(self.mne_data.compute_tfr(method='morlet',
                                                             freqs=self.frequencies(),
                                                             tmin=t_min, tmax=t_max,
                                                             n_jobs=-1,
                                                             verbose='CRITICAL',
                                                             n_cycles=self.frequencies()).get_data())

    def frequencies(self):
        """
        Return the interest frequencies:
        0.5 - 3.5 -> Delta
        3.5 - 7.5 -> Theta
        7.5 - 12.5 -> Alpha
        12.5 - 30 -> Beta
        30 - 60 -> Low Gamma
        60 - 128 -> High Gamma
        """
        return np.array([0.5, 3.5, 7.5, 12.5, 30, 60, 128])
