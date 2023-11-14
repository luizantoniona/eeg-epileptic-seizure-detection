import numpy as np
from scipy.signal import spectrogram
import math

class RawSignalModel:
    def __init__(self, channels_names, channels_frequencies, channels_buffers, times):
        self.channels_names = channels_names
        self.channels_frequencies = channels_frequencies
        self.channels_buffers = channels_buffers
        self.times = times

    def __str__(self):
        return f"{self.channels_names}"
    
    def segment_signals(self, seconds_to_segment: int = 10):

        buffer_len = len(buffer)

        number_of_points = self.channels_frequencies * seconds_to_segment
        number_of_samples = math.floor( buffer_len / number_of_points )

        segments = []

        for buffer in self.channels_buffers:

            buffer_len = len(buffer)

            for sample in range(0, number_of_samples):
                segments.append() # TODO: AJUSTAR

        self.segments = segments
    
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
            f, t, Sxx = spectrogram(buffer, Fs=self.channels_frequencies)
            spectograms.append((f, t, Sxx))

        self.channels_spectograms = spectograms

    def number_of_signals(self) -> int:
        return len(self.channels_names)
    
    def shape_of_buffers(self):
        return np.shape(self.channels_buffers)
    
    def shape_of_psds(self):
        return np.shape(self.channels_psds)
    
    def shape_of_spectograms(self):
        return np.shape(self.channels_spectograms)
