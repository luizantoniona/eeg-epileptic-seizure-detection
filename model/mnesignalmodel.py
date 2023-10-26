import mne
import numpy as np
class MNESignalModel:
    def __init__(self, mne_object: mne.io.Raw ):

        self.time_data = mne_object

        self.power_spectrum = mne_object.copy().compute_psd()

    def __str__(self):
        return f"{self.mne_object}"