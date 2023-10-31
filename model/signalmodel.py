class SignalModel:
    def __init__(self, channels_names, channels_frequencies, channels_buffers, times):
        self.channels_names = channels_names
        self.channels_frequencies = channels_frequencies
        self.channels_buffers = channels_buffers
        self.times = times

    def __str__(self):
        return f"{self.channels_names}"
