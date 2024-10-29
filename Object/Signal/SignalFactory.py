import mne
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Object.Signal.Signal import Signal
from Object.Signal.Frequency.PSDWelchSignal import PSDWelchSignal
from Object.Signal.Frequency.PSDMultitaperSignal import PSDMultitaperSignal
from Object.Signal.Time.TimeSignal import TimeSignal
from Object.Signal.TimeFrequency.SpectrogramSignal import SpectrogramSignal


def signal_by_type(signal_type: SignalTypeEnum, mne_object: mne.io.BaseRaw) -> Signal:
    match signal_type:
        case SignalTypeEnum.Time:
            return TimeSignal(mne_object)

        case SignalTypeEnum.PSDWelch:
            return PSDWelchSignal(mne_object)

        case SignalTypeEnum.PSDMultitaper:
            return PSDMultitaperSignal(mne_object)

        case SignalTypeEnum.Spectrogram:
            return SpectrogramSignal(mne_object)

        case _:
            return Signal(mne_object)
