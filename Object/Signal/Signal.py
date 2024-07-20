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

    def __init__(self, mne_object: mne.io.Raw):
        self.mne_data: mne.io.Raw = mne_object

        self.data = None
        self.data_segmented = []
        self.label_segmented = []

    def get_data(self):
        return self.data

    def get_data_segmented(self):
        return self.data_segmented

    def get_label_segmented(self):
        return self.label_segmented
    
    def generate_data(self):
        raise NotImplementedError()
    
    def generate_segmented_data(self):
        raise NotImplementedError()

    def delete_mne_data(self):
        """
        Delete mne_data from memory.
        """
        del self.mne_data
        self.mne_data = None
        gc.collect()
