import typing as t
from spectrum import pmtm, dpss
import numpy as np

class SignalTransform:

    __ps = None

    def __init__(self, signal: t.Optional[np.ndarray], Fs = 128.0, nw = 2.5, k = None):
        self.signal = signal
        self.Fs = Fs
        self.nw = nw
        self.k = k

        if self.k == None:
            self.k = int(self.nw * 2)

    def __get_psd(self, sig, data_taper = None, eigen = None):
        ps = None

        if (data_taper is not None) and (eigen is not None):
            ps, w, _ = pmtm(sig, e = eigen, v = data_taper, show = False)
        else:
            ps, w, _ = pmtm(self.signal, NW = self.nw, k = self.k, show = False)

        l = len(sig)
        ps = ps[:, 0 : l]
        w = w[0 : l, :]

        ps = abs(ps)**2
        ps = ps.transpose()
        ps = np.mean(ps * w, axis = 1)

        return ps

    def get_power_spectrum(self, data_taper: t.Optional[np.ndarray] = None,
                           eigen: t.Optional[np.ndarray] = None):
        self.__ps = self.__get_psd(self.signal, data_taper, eigen)

        return self.__ps

    def get_spectrogram(self, window_len: int = 128,
                        data_taper: t.Optional[np.ndarray] = None,
                        eigen: t.Optional[np.ndarray] = None):
        sg = []

        if (data_taper is None) or (eigen is None):
            data_taper, eigen = dpss(window_len, NW = self.nw, k = self.k)

        if len(self.signal) >= window_len:

            for i in range(0, len(self.signal) - window_len + 1):
                sg.append(self.__get_psd(self.signal[i : i + window_len],
                                         data_taper, eigen))

        sg = np.asarray(sg)

        return sg.T


    def get_bispectrogram(self, data_taper: t.Optional[np.ndarray] = None,
                          eigen: t.Optional[np.ndarray] = None):
        if self.__ps is None:
            self.__ps = self.get_power_spectrum(data_taper, eigen)

        bs = np.zeros((int(len(self.__ps) / 2) - 1,
                       int(len(self.__ps) / 2) - 1))

        for i in range(0, len(bs)):
            for j in range(0, len(bs) - i):
                bs[i, j] = self.__ps[i] * self.__ps[j] * self.__ps[i + j]
                bs[j, i] = bs[i, j]
                bs[len(bs)- i - 1, len(bs[0]) - j - 1] = bs[i, j]
                bs[len(bs[0]) - j - 1, len(bs)- i - 1] = bs[i, j]

        return bs

class RawSignalModel:

    signals_and_transforms = []

    def __init__(self, channels_names, channels_frequencies, channels_buffers, times):
        self.channels_names = channels_names
        self.channels_frequencies = channels_frequencies
        self.channels_buffers = channels_buffers
        self.times = times

    def __str__(self):
        return f"{self.channels_names}"
