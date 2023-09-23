import pyedflib
import numpy as np
import pandas as pd
import mne
import numpy as np

def selected_channels():
  return [
    'P8-O2',
    'CZ-PZ',
    'T8-P8',
    'T7-P7',
    'FZ-CZ',
    'C3-P3',
    'P4-O2',
    'C4-P4',
    'FP1-F7',
    'F3-C3',
    'F4-C4',
    'P7-O1',
    'FP2-F8',
    'F7-T7',
    'FP2-F4',
    'FP1-F3',
    'P3-O1',
    'F8-T8'
  ]

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

def raw_data(summary_model, selected_channels = selected_channels()):
  try: 
    edf_file = pyedflib.EdfReader("./data/" + summary_model.record_name + "/" + summary_model.file_name)

    channel_names = edf_file.getSignalLabels()
    channel_freq = edf_file.getSampleFrequencies()

    sigbufs = np.zeros((edf_file.getNSamples()[0],len(selected_channels)))
    for i, channel in enumerate(selected_channels):
      sigbufs[:, i] = edf_file.readSignal(channel_names.index(channel))
    
    data_frame = pd.DataFrame(sigbufs, columns = selected_channels).astype('float32')
    
    index_increase = np.linspace(0,
                                 len(data_frame)/channel_freq[0],
                                 len(data_frame), endpoint=False)

    seconds = np.floor(index_increase).astype('uint16')

    data_frame['Time'] = seconds
    data_frame = data_frame.set_index('Time')
    data_frame.columns.name = 'Channel'

    return mne_object(data_frame,
                      channel_freq[0],
                      events = [[int(x) for x in summary_model.start_seizure], [int(x) for x in summary_model.end_seizure]]
                      if summary_model.nr_seizures > 0 else None)

  except:
    OSError
    return pd.DataFrame(), None