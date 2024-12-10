from Object.Signal.SignalTypeEnum import SignalTypeEnum
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, label: str, index, signal_type, sampling_rate):
    plt.figure(figsize=(10, 10))

    if signal_type == SignalTypeEnum.Time:
        signal_scaled = signal * 1e6
        time_axis = np.linspace(0, len(signal) / sampling_rate, len(signal))
        plt.plot(time_axis, signal_scaled, color="b")
        x_label = "Time (s)"
        y_label = "Amplitude (μV)"
        plt.xlim(0, time_axis[-1])

    else:
        # freqs = np.fft.rfftfreq(len(signal), d=1 / sampling_rate)
        plt.plot(signal, color="b")
        x_label = "Frequency (Hz)"
        y_label = "Power (dB)"
        plt.xlim(0, sampling_rate / 2)
        plt.ylim(0)

    plt.title(f"{signal_type.name} {label.capitalize()}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
