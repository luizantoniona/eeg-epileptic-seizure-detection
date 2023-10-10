from sklearn.model_selection import train_test_split

def data_spliter(X, y):
    #X = ... feature data
    #y = ... target data

    #will return X_train, X_test, y_train, y_test
    return train_test_split(X, y, test_size=0.3, random_state=42)