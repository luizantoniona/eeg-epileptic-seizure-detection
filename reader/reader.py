"""
Module: reader

This module provides functionality to read data from an EDF (European Data Format) file using MNE (MNE-Python) library,
with options to renaming channels and setting the montage.
"""

import mne
import numpy as np
import re
import reader.reader_commons as commons
import pyedflib
import pandas as pd

def rename_channels(mne_object: mne.io.Raw):
  replace_dict = {}
  drop_list = []
  for channel_name in mne_object.info['ch_names']:
      name_change = re.findall('\w+',channel_name)[0].title()
      if name_change in list(replace_dict.values()):
          drop_list.append(channel_name)
      else:
          replace_dict[channel_name] = name_change

  mne_object.drop_channels(drop_list)
  mne_object.rename_channels(replace_dict)
  mne_object.set_montage('standard_1020')

def read_edf(summary_model, rename = False):
  print('Reading:', summary_model.fullpath())
  
  mne_model = mne.io.read_raw_edf(summary_model.fullpath(), include=commons.selected_channels(), preload=True, verbose='CRITICAL')

  if summary_model.nr_seizures > 0:
    start_times = []
    duration = []
    event_name = []

    for seizure_index in range(summary_model.nr_seizures):
      start_times.append(summary_model.start_seizure[seizure_index])
      duration.append(summary_model.end_seizure[seizure_index] - summary_model.start_seizure[seizure_index])
      event_name.append('Anomaly - ' + str(seizure_index))

    mne_model.set_annotations(mne.Annotations(np.array(start_times),
                                              np.array(duration),
                                              np.array(event_name)))
    if( rename ):
      rename_channels(mne_model)

  return mne_model

def read_edf_pyedf(summary_model):
  print('Reading:', summary_model.fullpath())

  file = pyedflib.EdfReader(summary_model.fullpath())
  selected_channels = commons.selected_channels()

  channel_names = file.getSignalLabels()
  channel_freq = file.getSampleFrequencies()

  sigbufs = np.zeros((file.getNSamples()[0],len(selected_channels)))

  for i, channel in enumerate(selected_channels):
    sigbufs[:, i] += file.readSignal(channel_names.index(channel))
  
  df = pd.DataFrame(sigbufs, columns = selected_channels).astype('float32')
  index_increase = np.linspace(0,
                                len(df)/channel_freq[0],
                                len(df), endpoint=False)
  seconds = np.floor(index_increase).astype('uint16')

  df['Time'] = seconds
  df = df.set_index('Time')
  df.columns.name = 'Channel'

  info = mne.create_info(ch_names=list(df.columns), 
                         sfreq=channel_freq[0], 
                         ch_types=['eeg']*df.shape[-1])

  df = df.apply(lambda x: x*1e-6)
  data_T = df.transpose()
  
  mne_model = mne.io.RawArray(data_T, info)

  if summary_model.nr_seizures > 0:
    start_times = []
    duration = []
    event_name = []

    for seizure_index in range(summary_model.nr_seizures):
      start_times.append(summary_model.start_seizure[seizure_index])
      duration.append(summary_model.end_seizure[seizure_index] - summary_model.start_seizure[seizure_index])
      event_name.append('Anomaly - ' + str(seizure_index))

    mne_model.set_annotations(mne.Annotations(np.array(start_times),
                                              np.array(duration),
                                              np.array(event_name)))

  return mne_model