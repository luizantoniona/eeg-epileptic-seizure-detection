from Object.Signal.Signal import Signal
import mne

class PSDSignal(Signal):
    """
    A class representing a Power Spectral Density signal model.
    """

    def __init__(self, mne_object: mne.io.Raw):
        super().__init__(mne_object)

    def generate_data(self):
        """
        Generate PSD data for all file.
        """
        self.data = self.mne_data.copy().compute_psd(verbose=False).get_data()
    
    def generate_segmented_data(self, t_min, t_max):
        """
        Generate segmented PSD data for a specified time interval.
        """
        self.data_segmented.append(self.mne_data.compute_psd(tmin=t_min, tmax=t_max, verbose='CRITICAL').get_data())
    
    def generate_segmented_labels(self):
        return super().generate_segmented_labels()
