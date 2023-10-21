import numpy as np
import reader.readercommons as commons
import pyedflib

def raw_edf(summary_model):
    selected_channels = commons.selected_channels()

    edf_instance = pyedflib.EdfReader(summary_model.fullpath())

    channels_names = edf_instance.getSignalLabels()
    channels_freq = edf_instance.getSampleFrequencies()[0]

    for channel_name in channels_names:
        if channel_name not in selected_channels:
            channels_names.remove(channel_name)

    channels_buffers = []

    for i, channel in enumerate(selected_channels):
        channels_buffers.append(edf_instance.readSignal(channels_names.index(channel)))

    edf_instance.close()

    return channels_names, channels_freq, channels_buffers