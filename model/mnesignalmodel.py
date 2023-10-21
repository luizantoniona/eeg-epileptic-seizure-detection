class MNESignalModel:    
    def __init__(self, mne_object):
        self.time_data = mne_object
        self.power_spectrum = mne_object.copy().compute_psd()
        self.spectogram = "" #TODO: Calcular Espectro de Potência com o MNE