import mne
import numpy as np
import matplotlib.pyplot as plt
import Metric.EvaluatorConverter as Converter
from Database.DatabaseMetrics import DatabaseMetrics
from IA.NNBase import NNBase
from Preprocessor.Preprocessor import Preprocessor
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Utils.Graphics.Heatmap import plot_2d_heatmap
from Utils.Graphics.SignalPlot import plot_signal
from Preprocessor.Loader.Loader import Loader
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name

DATASET = dataset_enum_by_name("CHBMIT")
MODELS = [
    # neural_network_enum_by_name("RNN"),
    neural_network_enum_by_name("CNN"),
    # neural_network_enum_by_name("CRNN"),
]
DOMAINS = [
    # signal_enum_by_name("PSDWelch"),
    signal_enum_by_name("PSDMultitaper"),
]
WINDOWS = [
    # 5,
    10,
]


database = DatabaseMetrics()

for model in MODELS:
    for domain in DOMAINS:
        for window in WINDOWS:

            db_objects = database.metrics_by_model_domain_window(DATASET.name, model.name, domain.name, window)
            if db_objects == []:
                print(f"No data found for {model.name}, {domain.name}, window size {window}")
                continue

            evaluations = []
            for db_object in db_objects:
                evaluations.append(Converter.model_from_tuple(db_object))

            summaries = Loader.load_summary(dataset_type=DATASET, file_name="chb04_28.edf")
            mne.utils.set_log_level("CRITICAL")
            Loader.load_segmented_data(summaries, signal_type=SignalTypeEnum.Time, window_length=window, overlap_shift_size=window)
            signal_original = summaries[0].signal.get_data_segmented()
            labels_original = summaries[0].signal.get_label_segmented()
            signal_combined = np.concatenate(signal_original, axis=1)

            data, labels = Preprocessor.preprocess_with_file_name(dataset_type=DATASET, model_type=model, signal_type=domain, window_length=window, overlap_shift_size=window, file_name="chb04_28.edf")

            for evaluation in evaluations:
                modelNN = NNBase(0, 0)
                modelNN.load_model(f"data/Models/{DATASET.name}/{domain.name}/{model.name}/{window}/{evaluation.accuracy}.keras")

                modelNN.predict_classes(data)

                index = []

                for i in range(modelNN.predictions.size):
                    if modelNN.predictions[i] != bool(labels[i]):
                        index.append(i)

                print(f"Model: {model.name} | Domain: {domain.name} | Window: {window} | INDEXES: {index} | Acc: {evaluation.accuracy}")

                for i in range(summaries[0].get_nr_occurrence()):
                    print(f"START: {summaries[0].start_time_of_ocurrence(i)} | END: {summaries[0].end_time_of_ocurrence(i)}")

                for i in index:
                    plot_signal(signal_original[i], f"Model: {model.name} | Window: {window} | Index: {i} | GT: {bool(labels[i])} | PRED: {modelNN.predictions[i]}", SignalTypeEnum.Time, 256)
                    plot_signal(data[i], f"Model: {model.name} | Window: {window} | Index: {i} | GT: {bool(labels[i])} | PRED: {modelNN.predictions[i]}", domain, 256)
