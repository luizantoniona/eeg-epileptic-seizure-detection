import numpy as np
import matplotlib.pyplot as plt


def plot_2d_heatmap(spectrogram, label, index, signal_type, sampling_rate):

    frequency_vector = [0.5, 4, 8, 12, 16, 30, 60]

    num_time_points = spectrogram.shape[1]
    time_vector = np.arange(num_time_points) / sampling_rate

    plt.figure(figsize=(10, 10))
    plt.imshow(spectrogram, aspect="auto", cmap="viridis", origin="lower")
    plt.colorbar(label="Amplitude")
    plt.title(f"{signal_type.name} {label.capitalize()}")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.xticks(ticks=np.linspace(0, num_time_points - 1, num=5), labels=np.round(np.linspace(time_vector[0], time_vector[-1], num=5), 2))
    plt.yticks(ticks=np.linspace(0, len(frequency_vector) - 1, num=len(frequency_vector) - 1), labels=frequency_vector[0:6])
    plt.show()
