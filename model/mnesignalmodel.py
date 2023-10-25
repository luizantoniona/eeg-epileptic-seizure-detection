import mne
class MNESignalModel:    
    def __init__(self, mne_object: mne.io.Raw, epochs: mne.Epochs ):
        self.time_data = mne_object
        self.power_spectrum = mne_object.copy().compute_psd()
        self.epochs = epochs
        self.spectogram = "" #TODO: Calcular Espectro de Potência com o MNE

    def __str__(self):
        return f"{self.mne_object}"