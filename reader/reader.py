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

def mne_edf(summary_model):
  mne_model = mne.io.read_raw_edf(summary_model.fullpath(), include=selected_channels())

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

def mne_epochs(summary_model):
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