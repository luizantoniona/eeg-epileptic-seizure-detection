from spectrum import pmtm, dpss
import numpy as np
import typing as t

class SignalModel:
    def __init__(self, channels_names, channels_frequencies, channels_buffers, times, nw = 2.5, k = None):
        self.channels_names = channels_names
        self.channels_frequencies = channels_frequencies
        self.channels_buffers = channels_buffers
        self.times = times
        self.nw = nw
        self.k = k

        if self.k == None:
            self.k = int(self.nw * 2)

    def __str__(self):
        return f"{self.channels_names}"
        