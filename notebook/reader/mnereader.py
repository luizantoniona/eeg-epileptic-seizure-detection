import mne
import numpy as np

def mne_object(data, freq, events = None):
  info = mne.create_info(ch_names=list(data.columns), 
                         sfreq=freq, 
                         ch_types=['eeg']*data.shape[-1])
  
  data = data.apply(lambda x: x*1e-6)
  data_T = data.transpose()
  
  raw = mne.io.RawArray(data_T, info)

  if events:
    start_times = np.array(events[0])
    end_times = np.array(events[1])
    anno_length = end_times-start_times
    event_name = np.array(['Ictal']*len(anno_length))

    raw.set_annotations(mne.Annotations(start_times,
                                      anno_length,
                                      event_name))

  return raw