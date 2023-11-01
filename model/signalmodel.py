import numpy as np
import matplotlib.pyplot as plt
class SignalModel:
    def __init__(self, channels_names, channels_frequencies, channels_buffers, times):
        self.channels_names = channels_names
        self.channels_frequencies = channels_frequencies
        self.channels_buffers = channels_buffers
        self.times = times

    def __str__(self):
        return f"{self.channels_names}"
    
    def psd(self):
        psds = []

        for buffer in self.channels_buffers:
            fft_result = np.fft.fft(buffer)
            espectro_potencia = np.abs(fft_result)**2 / len(buffer)
            psds.append(espectro_potencia)

        self.channels_psds = psds

    def spc(self):
        spectograms = []
        
        for buffer in self.channels_buffers:
            f, t, Sxx = plt.specgram(buffer, Fs=self.channels_frequencies)
            spectograms.append((f, t, Sxx))

        self.channels_spectograms = spectograms
