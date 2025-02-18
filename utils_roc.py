import Metric.EvaluatorConverter as Converter
from Database.DatabaseMetrics import DatabaseMetrics
from IA.NNBase import NNBase
from Preprocessor.Preprocessor import Preprocessor
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name
from Utils.Graphics.ROCPlotter import ROCPlotter

DATASET = dataset_enum_by_name("CHBMIT")
MODEL = neural_network_enum_by_name("CNN")
DOMAIN = signal_enum_by_name("PSDWelch")
windows = [1, 2, 5, 10]
colors = ["r", "g", "b", "y"]

plotter = ROCPlotter()

for window, color in zip(windows, colors):
    database = DatabaseMetrics()
    db_object = database.higher_metrics_by_model_domain_window(DATASET.name, MODEL.name, DOMAIN.name, window)

    if db_object is None:
        print(f"No data found for {MODEL.name}, {DOMAIN.name}, window size {window}")
        continue

    evaluation = Converter.model_from_tuple(db_object)

    data, labels = Preprocessor.preprocess_with_size(dataset_type=DATASET, model_type=MODEL, signal_type=DOMAIN, window_length=window, nr_files=10)

    model = NNBase(0, 0)
    model.load_model(f"data/Models/{DATASET.name}/{DOMAIN.name}/{MODEL.name}/{window}/{evaluation.accuracy}.keras")

    model.predict(data)

    plotter.add_curve(labels, model.predictions, label=f"{MODEL.name} {DOMAIN.name} {window}", color=color)

    del data
    del labels
    del model

plotter.plot()
