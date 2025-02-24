from Dataset.DatasetTypeEnum import DatasetTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Preprocessor.Loader.Loader import Loader
from Utils.Graphics.Heatmap import plot_2d_heatmap
from Utils.Graphics.SignalPlot import plot_signal
import mne

DATASET_TYPE = DatasetTypeEnum.CHBMIT
SIGNAL_TYPE = SignalTypeEnum.Time
WINDOW_LENGTH = 5

summaries = Loader.load_anomalous_summaries(DATASET_TYPE)

summary = summaries[10]

mne.utils.set_log_level("CRITICAL")

Loader.load_segmented_data([summary], signal_type=SIGNAL_TYPE, window_length=WINDOW_LENGTH)

signal = summary.signal.get_data_segmented()
labels = summary.signal.get_label_segmented()

size = len(signal)
quarter = int(size / 4)

indexes = [0 * quarter, 1 * quarter, 2 * quarter, 3 * quarter]

for i in indexes:
    index = int(i + (quarter / 2))
    print("Index:", index)
    if SIGNAL_TYPE == SignalTypeEnum.Spectrogram:
        plot_2d_heatmap(signal[index][0], labels[index], index, SIGNAL_TYPE, 256)

    else:
        plot_signal(signal[index][0], labels[index], SIGNAL_TYPE, 256)
