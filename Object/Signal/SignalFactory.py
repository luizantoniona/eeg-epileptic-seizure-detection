from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Object.Signal.Signal import Signal
from Object.Signal.Frequency.PSDSignal import PSDSignal
from Object.Signal.Time.TimeSignal import TimeSignal
from Object.Signal.TimeFrequency.SpectrogramSignal import SpectrogramSignal
import mne

def signal_by_type(signal_type: SignalTypeEnum, mne_object: mne.io.Raw) -> Signal:
    match signal_type:
        case SignalTypeEnum.Time:
            return TimeSignal(mne_object)

        case SignalTypeEnum.PSD:
            return PSDSignal(mne_object)

        case SignalTypeEnum.Spectrogram:
            return SpectrogramSignal(mne_object)

        case _:
            return Signal(mne_object)
