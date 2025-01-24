"""
Module: Trainer
"""

import os
import gc
import keras_tuner as kt
import keras
import time
import IA.NeuralNetworkModelFactory as NNModelFactory
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from Dataset.DatasetTypeEnum import DatasetTypeEnum
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
from IA.NNBase import NNBase
from Metric.Metric import Metric
from Object.Signal.SignalTypeEnum import SignalTypeEnum

NR_EPOCHS = 100
BATCH_SIZE = 16


class Trainer:
    @staticmethod
    def train(dataset_type: DatasetTypeEnum, model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int, data, labels):

        try:
            data_opt, data_rest, labels_opt, labels_rest = train_test_split(data, labels, test_size=0.8, random_state=42)

            best_hps = Trainer.optimize_hyperparameters(dataset_type, model_type, signal_type, window_length, data_opt, labels_opt)

            del data_opt, labels_opt
            gc.collect()

            data_train, data_test, labels_train, labels_test = train_test_split(data_rest, labels_rest, test_size=0.2, random_state=42)

            del data_rest, labels_rest
            gc.collect()

            kf = KFold(n_splits=10)

            for train_index, val_index in kf.split(data_train):
                Trainer.clear_memory()

                X_train, X_val = data_train[train_index], data_train[val_index]
                y_train, y_val = labels_train[train_index], labels_train[val_index]

                neural_network_model = Trainer.build_and_compile_model(model_type, signal_type, window_length, data_train[0].shape, best_hps)
                neural_network_model.fit(X_train, y_train, num_epochs=NR_EPOCHS, batch_size=BATCH_SIZE, val_data=X_val, val_labels=y_val)
                neural_network_model.predict_classes(data_test)

                Trainer.evaluate_metrics(labels_test, dataset_type, model_type, signal_type, window_length, neural_network_model)

        except Exception as e:
            print(f"FAILED {e}")

    @staticmethod
    def optimize_hyperparameters(dataset_type: DatasetTypeEnum, model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int, data, labels):

        data_train, data_val, labels_train, labels_val = train_test_split(data, labels, test_size=0.2, random_state=42)

        def build(hp):
            neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, data_train[0].shape, window_length)
            neural_network_model.construct_model(hp)
            neural_network_model.compile(hp)
            return neural_network_model.model

        tuner = kt.BayesianOptimization(
            build,
            objective="val_accuracy",
            max_trials=20,
            max_consecutive_failed_trials=2,
            directory="data/Tuner",
            project_name=f"{dataset_type.name}/{signal_type.name}/{model_type.name}/{window_length}",
        )

        success: bool = False
        max_attempts: int = 3
        attempts: int = 0

        while not success and attempts < max_attempts:
            try:
                tuner.search_space_summary()
                tuner.search(data_train, labels_train, epochs=50, batch_size=BATCH_SIZE, validation_data=(data_val, labels_val))
                success = True

            except Exception as e:
                Trainer.clear_memory()
                attempts += 1
                if attempts >= max_attempts:
                    raise e

        best_hps = tuner.get_best_hyperparameters()[0]
        return best_hps

    @staticmethod
    def build_and_compile_model(model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int, input_shape, best_hps):
        neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, input_shape, window_length)
        neural_network_model.construct_model(best_hps)
        neural_network_model.compile(best_hps)
        neural_network_model.summary()
        return neural_network_model

    @staticmethod
    def save_model(dataset_type: DatasetTypeEnum, model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int, accuracy: float, neural_network_model: NNBase):
        model_dir = f"data/Models/{dataset_type.name}/{signal_type.name}/{model_type.name}/{window_length}"
        os.makedirs(model_dir, exist_ok=True)
        model_filepath = f"{model_dir}/{str(accuracy)}.keras"
        neural_network_model.save_model(filepath=model_filepath)

    @staticmethod
    def evaluate_metrics(y_val, dataset_type: DatasetTypeEnum, model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int, neural_network_model: NNBase):
        metric = Metric(y_val, neural_network_model.predictions, dataset_name=dataset_type.name, model_name=model_type.name, model_data_domain=signal_type.name, model_window_length=window_length)
        metric.all_metrics()
        metric.metrics_to_database()
        Trainer.save_model(dataset_type, model_type, signal_type, window_length, metric.accuracy, neural_network_model)

    @staticmethod
    def clear_memory():
        keras.backend.clear_session()
        gc.collect()
        time.sleep(1)
