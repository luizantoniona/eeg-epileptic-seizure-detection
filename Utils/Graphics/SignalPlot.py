from Object.Signal.SignalTypeEnum import SignalTypeEnum
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, label: str, signal_type, sampling_rate):
    """
    Plots EEG signals in time or frequency domain.

    - If `signal` has multiple channels (shape: [channels, time]), each channel is plotted separately.
    - If `signal` is 1D, it is plotted normally.
    """
    if signal_type == SignalTypeEnum.Time:
        num_channels = signal.shape[0] if signal.ndim >= 2 else 1
        fig, axes = plt.subplots(num_channels, 1, figsize=(12, 6), sharex=True, sharey=True)

        if num_channels == 1:
            axes = [axes]

        time_axis = np.linspace(0, signal.shape[1] / sampling_rate, signal.shape[1])

        for ch in range(num_channels):
            ch_signal = signal[ch] * 1e6 if num_channels > 1 else signal * 1e6
            axes[ch].plot(time_axis, ch_signal, label=f"Channel {ch+1}")
            axes[ch].grid(True)

        x_label = "Time (s)"
        fig.suptitle(f"{signal_type.name} - {label}")

        fig.text(0.04, 0.5, "Amplitude", va="center", ha="center", rotation="vertical")

        for ax in axes:
            ax.set_xlabel(x_label)
            ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

        plt.tight_layout()
        plt.show()

    else:
        num_channels = signal.shape[0] if signal.ndim >= 2 else 1
        plt.figure(figsize=(12, 6))

        for ch in range(num_channels):
            plt.plot(signal[ch], label=f"Channel {ch+1}")

        x_label = "Frequency (Hz)"
        y_label = "Power (dB)"
        plt.xlim(0, sampling_rate / 2)
        plt.ylim(bottom=0)
        plt.title(f"{signal_type.name} - {label}")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True)
        plt.show()
