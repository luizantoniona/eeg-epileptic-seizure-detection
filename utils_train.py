from Preprocessor.Preprocessor import Preprocessor
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name
from Trainer.Trainer import Trainer


DATASET = dataset_enum_by_name("CHBMIT")
MODEL = neural_network_enum_by_name("CRNN")
DOMAIN = signal_enum_by_name("PSDWelch")
WINDOW = 10


def run():
    print("PREPROCESSOR STARTED")
    data, labels = Preprocessor.preprocess(dataset_type=DATASET, model_type=MODEL, signal_type=DOMAIN, window_length=WINDOW)
    print("PREPROCESSOR FINISHED")

    print("TRAINING STARTED")
    Trainer.train(dataset_type=DATASET, model_type=MODEL, signal_type=DOMAIN, window_length=WINDOW, data=data, labels=labels)
    print("TRAINING FINISHED")


run()
