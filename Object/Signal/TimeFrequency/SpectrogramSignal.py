from Object.Signal.Signal import Signal
import gc
import mne
import numpy as np


class SpectrogramSignal(Signal):
    """
    A class representing a Spectrogram signal model.
    """

    def __init__(self, mne_object: mne.io.BaseRaw):
        super().__init__(mne_object)

    def generate_data(self):
        """
        Generate Spectrogram data for all file.
        """
        spectrogram = self.mne_data.compute_tfr(method="multitaper", freqs=self.frequencies(), n_jobs=4, n_cycles=self.frequencies())

        self.data = spectrogram.get_data()
        del spectrogram
        gc.collect()

    def generate_segmented_data(self, t_min, t_max):
        """
        Generate segmented Spectrogram data for a specified time interval.
        """
        spectrogram = self.mne_data.compute_tfr(method="multitaper", freqs=self.frequencies(), tmin=t_min, tmax=t_max, n_jobs=4, n_cycles=self.frequencies())

        self.data_segmented.append(spectrogram.get_data())
        del spectrogram
        gc.collect()

    def frequencies(self):
        """
        Return the interest frequencies:
        0.5 - 3.5 -> Delta
        3.5 - 7.5 -> Theta
        7.5 - 12.5 -> Alpha
        12.5 - 30 -> Beta
        30+ -> Gamma
        """
        return np.arange(1, 60, 10)
