"""
"""
import Preprocessor.Balancer.Balancer as Balancer
import Preprocessor.Loader.Loader as Loader
import Preprocessor.Normalizer.Normalizer as Normalizer
import Preprocessor.Splitter.time_splitter as splitter
import random

def preprocess( train_split, validation_split, test_split, 
                balance_train = False, balance_val = False, balance_test = False ):

    summaries = Loader.load_anomalous_summaries()

    Loader.load_time_segmented_data(summaries)

    Normalizer.normalize(summaries)

    # random.shuffle(summaries)

    # X_train, X_val, y_train, y_val = splitter.train_val_segmented_time_data(summaries[:number_train_val_samples])

    # X_test, y_test = splitter.test_segmented_time_data(summaries[number_train_val_samples + 1 : number_train_val_samples + 1 + number_test_samples])

    if( balance_train ):
        X_train, y_train = Balancer.balance(X_train, y_train)

    if( balance_val ):
        X_validation, y_validation = Balancer.balance(X_validation, y_validation)
    
    if ( balance_test ):
        X_test, y_test = Balancer.balance(X_test, y_test)

    return X_train, y_train, X_validation, y_validation, X_test, y_test
