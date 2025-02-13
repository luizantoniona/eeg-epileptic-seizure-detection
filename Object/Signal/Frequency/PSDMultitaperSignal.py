from Object.Signal.Signal import Signal
import gc
import mne


class PSDMultitaperSignal(Signal):
    """
    A class representing a Power Spectral Density signal model.
    """

    def __init__(self, mne_object: mne.io.BaseRaw):
        super().__init__(mne_object)

    def generate_data(self):
        """
        Generate PSD data for all file.
        """
        psd = self.mne_data.compute_psd(method="multitaper", n_jobs=4)

        self.data = psd.get_data()
        del psd
        gc.collect()

    def generate_segmented_data(self, t_min, t_max):
        """
        Generate segmented PSD data for a specified time interval.
        """
        psd = self.mne_data.compute_psd(method="multitaper", tmin=t_min, tmax=t_max, n_jobs=4)

        self.data_segmented.append(psd.get_data())
        del psd
        gc.collect()
