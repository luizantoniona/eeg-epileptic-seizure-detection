import tensorflow as tf
class CNNModel:

    def __init__(self, channel_buffers, num_channels):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=(channel_buffers, num_channels)))
        self.model.add(tf.keras.layers.MaxPooling1D(2))
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(2))
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, val_data, val_labels):
        self.model.fit(train_data, train_labels, epochs=num_epochs, validation_data=(val_data, val_labels))