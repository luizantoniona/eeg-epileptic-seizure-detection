from Object.Signal.Frequency.PSDSignal import PSDSignal
from Object.Signal.Signal import Signal
from Object.Signal.Time.TimeSignal import TimeSignal
import mne

def signal_by_type(signal_type: str, mne_object: mne.io.Raw ):
    if signal_type == "time":
        return TimeSignal(mne_object)
    
    elif signal_type == "PSD":
        return PSDSignal(mne_object)
    
    else:
        return Signal(mne_object)