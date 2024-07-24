"""
Module: Preprocessor
"""
import mne
import random
import Preprocessor.Balancer.Balancer as Balancer
import Preprocessor.Loader.Loader as Loader
import Preprocessor.Normalizer.Normalizer as Normalizer
import Preprocessor.Splitter.Splitter as Splitter

def preprocess( signal_type : str, window_length: int,
                balance_train = True, balance_val = True, balance_test = True,
                train_size=0.70, val_size=0.20, test_size=0.10 ):
    """
    Preprocess the data by loading, normalizing, splitting, and balancing it.

    Args:
        signal_type (str): Type of signal to load.
        balance_train (bool): Whether to balance the training data.
        balance_val (bool): Whether to balance the validation data.
        balance_test (bool): Whether to balance the test data.
        train_size (float): Proportion of data to use for training.
        val_size (float): Proportion of data to use for validation.
        test_size (float): Proportion of data to use for testing.

    Returns:
        tuple: Processed data split into training, validation, and test sets.
    """
    summaries = Loader.load_anomalous_summaries()

    mne.set_log_level("CRITICAL")

    random.shuffle(summaries)

    Loader.load_segmented_data(summaries, signal_type=signal_type, window_length=window_length)

    Normalizer.normalize(summaries)

    X_train, y_train, X_validation, y_validation, X_test, y_test = Splitter.split(summaries, train_size, val_size, test_size)

    if( balance_train ):
        X_train, y_train = Balancer.balance(X_train, y_train)

    if( balance_val ):
        X_validation, y_validation = Balancer.balance(X_validation, y_validation)
    
    if ( balance_test ):
        X_test, y_test = Balancer.balance(X_test, y_test)

    print("TRAIN SHAPE:", X_train.shape)
    print("VALIDATION SHAPE:", X_validation.shape)
    print("TEST SHAPE:", X_test.shape)

    return X_train, y_train, X_validation, y_validation, X_test, y_test