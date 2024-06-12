from Object.Signal.Signal import Signal
from Object.Signal.Frequency.PSDSignal import PSDSignal
from Object.Signal.Time.TimeSignal import TimeSignal
from Object.Signal.TimeFrequency.SpectogramSignal import SpectogramSignal
import mne

def signal_by_type(signal_type: str, mne_object: mne.io.Raw ):
    if signal_type == "time":
        return TimeSignal(mne_object)
    
    elif signal_type == "PSD":
        return PSDSignal(mne_object)
    
    elif signal_type == "spectogram":
        return SpectogramSignal(mne_object)

    else:
        return Signal(mne_object)
