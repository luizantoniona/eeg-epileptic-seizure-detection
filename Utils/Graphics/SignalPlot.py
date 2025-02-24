from Object.Signal.SignalTypeEnum import SignalTypeEnum
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, label: str, signal_type, sampling_rate):
    """
    Plots EEG signals in time or frequency domain.

    - If `signal` has multiple channels (shape: [channels, time]), each channel is plotted separately.
    - If `signal` is 1D, it is plotted normally.
    """
    plt.figure(figsize=(12, 6))

    if signal_type == SignalTypeEnum.Time:
        time_axis = np.linspace(0, signal.shape[1] / sampling_rate, signal.shape[1])

        num_channels = signal.shape[0] if signal.ndim >= 2 else 1

        for ch in range(num_channels):
            ch_signal = signal[ch] * 1e6 if num_channels > 1 else signal * 1e6
            plt.plot(time_axis, ch_signal + ch * 10, label=f"Channel {ch+1}")

        x_label = "Time (s)"
        y_label = "Amplitude (μV)"
        plt.xlim(0, time_axis[-1])

    else:
        num_channels = signal.shape[0] if signal.ndim >= 2 else 1

        for ch in range(num_channels):
            plt.plot(signal[ch], label=f"Channel {ch+1}")

        x_label = "Frequency (Hz)"
        y_label = "Power (dB)"
        plt.xlim(0, sampling_rate / 2)
        plt.ylim(bottom=0)

    plt.title(f"{signal_type.name} - {label.capitalize()}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.show()
