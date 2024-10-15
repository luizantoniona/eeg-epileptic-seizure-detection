import gc
import mne


class Signal:
    """
    A class representing an MNE signal model.

    Attributes:
    ----------
    mne_data : mne.io.Raw
        MNE raw data object.
    data : None
        Placeholder for processed data.
    data_segmented : list
        List to store segmented data.
    label_segmented : list
        List to store labels about data segments.
    """

    def __init__(self, mne_object: mne.io.BaseRaw):
        self.mne_data: mne.io.BaseRaw = mne_object

        self.data = None
        self.data_segmented: list = []
        self.label_segmented: list = []

    def get_data(self):
        return self.data

    def get_data_segmented(self):
        return self.data_segmented

    def get_label_segmented(self):
        return self.label_segmented

    def generate_data(self):
        raise NotImplementedError()

    def generate_segmented_data(self, t_min, t_max):
        raise NotImplementedError()

    def delete_mne_data(self):
        """
        Delete mne_data from memory.
        """
        if self.mne_data is not None:
            self.mne_data.close()
            del self.mne_data
            gc.collect()
