import mne
class MNESignalModel:    
    def __init__(self, mne_object: mne.io.Raw ):
        self.time_data = mne_object
        self.power_spectrum = mne_object.copy().compute_psd()
        self.spectogram = "" #TODO: Calcular Espectro de Potência com o MNE

    def __str__(self):
        return f"{self.mne_object}"