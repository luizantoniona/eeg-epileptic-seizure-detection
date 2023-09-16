import pyedflib
import numpy as np
import pandas as pd

def raw_data(summary_model, selected_channels = []):
  try: 

    edf_file = pyedflib.EdfReader("../data/" + summary_model.record_name + "/" + summary_model.file_name)
    
    if len(selected_channels) == 0:
      selected_channels = edf_file.getSignalLabels()

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

    return data_frame, channel_freq[0]

  except:
    OSError
    return pd.DataFrame(), None