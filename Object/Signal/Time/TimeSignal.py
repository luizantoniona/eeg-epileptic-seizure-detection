from Object.Signal.Signal import Signal
import mne

class TimeSignal(Signal):
    """
    A class representing a time signal model.
    """

    def __init__(self, mne_object: mne.io.Raw):
        super().__init__(mne_object)

    def generate_data(self):
        """
        Generate time data for all file.
        """
        self.data = self.mne_data.get_data()
    
    def generate_segmented_data(self, t_min, t_max):
        """
        Generate segmented time data for a specified time interval.
        """
        self.data_segmented.append(self.mne_data.get_data(tmin=t_min, tmax=t_max))
