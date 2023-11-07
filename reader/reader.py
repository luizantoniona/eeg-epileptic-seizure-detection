import numpy as np
import reader.readercommons as commons
import pyedflib

def edf(summary_model):
    selected_channels = commons.selected_channels()

    edf_instance = pyedflib.EdfReader(summary_model.fullpath())

    channels_names = edf_instance.getSignalLabels()
    channels_freq = edf_instance.getSampleFrequencies()[0]

    channels_buffers = np.zeros((len(selected_channels), edf_instance.getNSamples()[0]))

    adjust_resolution = np.vectorize(lambda x: x*1e-6)

    for i, channel in enumerate(selected_channels):
      channels_buffers[i, :] = adjust_resolution( edf_instance.readSignal(channels_names.index(channel)) )

    times = np.linspace(0, len(channels_buffers[0])/channels_freq, len(channels_buffers[0]), endpoint=False)

    edf_instance.close()

    del edf_instance
    del channels_names
    del adjust_resolution

    return selected_channels, channels_freq, channels_buffers, times