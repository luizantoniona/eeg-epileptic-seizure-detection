"""
Module: Reader

This module provides functionality to read data from an EDF (European Data Format) file using MNE (MNE-Python) library,
with options to renaming channels and setting the montage.
"""

import mne
import numpy as np
import re
import Reader.ReaderCommons as Commons
from Object.Summary import Summary


def rename_channels(mne_object: mne.io.BaseRaw):
    replace_dict = {}
    drop_list = []
    for channel_name in mne_object.info["ch_names"]:
        name_change = re.findall("\\w+", channel_name)[0].title()
        if name_change in list(replace_dict.values()):
            drop_list.append(channel_name)
        else:
            replace_dict[channel_name] = name_change

    mne_object.drop_channels(drop_list)
    mne_object.rename_channels(replace_dict)
    mne_object.set_montage("standard_1020")


def read_edf(summary_model: Summary, rename=False):
    mne_model = mne.io.read_raw_edf(summary_model.fullpath(), include=Commons.selected_channels(), preload=False, verbose="critical")

    mne_model.drop_channels(Commons.remove_channels(), on_missing="ignore")

    if "T8-P8-0" in mne_model.info["ch_names"]:
        mne_model.rename_channels(Commons.rename_channels())

    mne_model.reorder_channels(Commons.selected_channels())

    if summary_model.nr_occurrence > 0:
        start_times = []
        duration = []
        event_name = []

        for ocurrence_index in range(summary_model.nr_occurrence):
            start_times.append(summary_model.start_occurrence[ocurrence_index])
            duration.append(summary_model.end_occurrence[ocurrence_index] - summary_model.start_occurrence[ocurrence_index])
            event_name.append("Anomaly - " + str(ocurrence_index))

        mne_model.set_annotations(mne.Annotations(np.array(start_times), np.array(duration), np.array(event_name)))
        if rename:
            rename_channels(mne_model)

    return mne_model
