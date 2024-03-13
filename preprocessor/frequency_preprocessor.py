"""
"""
import random
import loader.data_loader as loader
import normalizer.frequency_normalizer as normalizer
import splitter.frequency_splitter as splitter
import balancer.data_balancer as balancer

def preprocess( balance_train = False, balance_val = False, balance_test = False, number_test_samples = 5 ):

    summaries = loader.load_anomalous_summaries()

    number_train_val_samples = len(summaries) - number_test_samples

    random.shuffle(summaries)

    loader.load_freq_segmented_data(summaries)

    normalizer.normalize_frequency_data(summaries)

    X_train, X_val, y_train, y_val = splitter.train_val_segmented_frequency_data(summaries[:number_train_val_samples])

    X_test, y_test = splitter.test_segmented_frequency_data(summaries[number_train_val_samples + 1 : number_train_val_samples + 1 + number_test_samples])

    if( balance_train ):
        X_train, y_train = balancer.balance(X_train, y_train)

    if( balance_val ):
        X_val, y_val = balancer.balance(X_val, y_val)
    
    if ( balance_test ):
        X_test, y_test = balancer.balance(X_test, y_test)

    return X_train, y_train, X_val, y_val, X_test, y_test