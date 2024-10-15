import keras
import numpy as np


class TrainingDropMonitor(keras.callbacks.Callback):
    """
    Custom callback to stop training if the monitored metric drops by more than a specified delta.
    """

    def __init__(self, monitor="val_accuracy", min_delta=0.2, patience=1):
        super(TrainingDropMonitor, self).__init__()
        self.monitor = monitor
        self.min_delta = min_delta
        self.patience = patience
        self.previous = None
        self.best_weights = None
        self.best = -np.Inf
        self.wait = 0

    def on_epoch_end(self, epoch, logs=None):
        current = logs.get(self.monitor)
        if current is None:
            return

        if self.previous is None:
            self.previous = current
            return

        if current > self.best:
            self.best = current
            self.best_weights = self.model.get_weights()
            self.wait = 0

        if current < self.previous - self.min_delta:
            self.wait += 1
            print(f"Warning: {self.monitor} dropped by more than {self.min_delta * 100}% on epoch {epoch + 1}")

            if self.wait >= self.patience:
                self.model.stop_training = True
                self.model.set_weights(self.best_weights)
                print(f"Stopping training early. {self.monitor} dropped significantly. Restoring best weights from epoch {epoch - self.patience + 1}.")
        else:
            self.wait = 0

        self.previous = current

    def on_train_end(self, logs=None):
        if self.best_weights is not None:
            self.model.set_weights(self.best_weights)
            print("Restored model to best weights from training.")
