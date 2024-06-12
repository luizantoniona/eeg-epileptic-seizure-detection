"""
Module: Preprocessor
"""
import random
import Preprocessor.Balancer.Balancer as Balancer
import Preprocessor.Loader.Loader as Loader
import Preprocessor.Normalizer.Normalizer as Normalizer
import Preprocessor.Splitter.Splitter as Splitter

def preprocess( signal_type : str,
                balance_train = False, balance_val = False, balance_test = False, 
                train_size=0.70, val_size=0.20, test_size=0.10 ):
    """
    """
    summaries = Loader.load_anomalous_summaries()

    Loader.load_segmented_data(summaries, signal_type=signal_type)

    Normalizer.normalize(summaries)

    random.shuffle(summaries)

    X_train, y_train, X_validation, y_validation, X_test, y_test = Splitter.split(summaries, train_size, val_size, test_size)

    if( balance_train ):
        X_train, y_train = Balancer.balance(X_train, y_train)

    if( balance_val ):
        X_validation, y_validation = Balancer.balance(X_validation, y_validation)
    
    if ( balance_test ):
        X_test, y_test = Balancer.balance(X_test, y_test)

    print(X_train.shape)
    print(X_validation.shape)
    print(X_test.shape)

    return X_train, y_train, X_validation, y_validation, X_test, y_test