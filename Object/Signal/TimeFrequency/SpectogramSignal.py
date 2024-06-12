from Object.Signal.Signal import Signal
import mne
import numpy as np

class SpectogramSignal(Signal):
    """
    A class representing a Spectogram signal model.
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
                                                     n_cycles=self.frequencies()/2 ).get_data()

    def generate_segmented_data(self, t_min, t_max):
        """
        Generate segmented Spectogram data for a specified time interval.
        """
        self.data_segmented.append(self.mne_data.compute_tfr(method='morlet',
                                                             freqs=self.frequencies(),
                                                             tmin=t_min, tmax=t_max,
                                                             n_jobs=-1,
                                                             verbose='CRITICAL',
                                                             n_cycles=self.frequencies()/2 ).get_data())

    def frequencies(self):
        return np.arange(1.0, 128.0, 8.0)
