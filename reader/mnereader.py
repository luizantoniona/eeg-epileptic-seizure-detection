import model.summarymodel as sm
import mne
import numpy as np
import re
import reader.readercommons as commons

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

def mne_edf(summary_model: sm.SummaryModel, rename = False):
  mne_model = mne.io.read_raw_edf(summary_model.fullpath(), include=commons.selected_channels())

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

def mne_epochs(summary_model: sm.SummaryModel):
  metadata_tmin, metadata_tmax = 0, summary_model.duration()
  
  edf_raw_object = mne_edf(summary_model)

  all_events, all_event_id = mne.events_from_annotations(edf_raw_object)

  events = mne.epochs.make_metadata(
    events=all_events,
    event_id=all_event_id,
    tmin=metadata_tmin,
    tmax=metadata_tmax,
    sfreq=edf_raw_object.info["sfreq"],
  )[1]

  return mne.Epochs(edf_raw_object, events)