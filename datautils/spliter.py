import model.summarymodel as sm
import numpy as np
from sklearn.model_selection import train_test_split

def time_data_spliter(summaries: list[sm.SummaryModel]):

    X_train, X_val = train_test_split(summaries, test_size=0.2, random_state=42)

    X_train_raw = [summarie.signal.channels_buffers for summarie in X_train]
    X_val_raw = [summarie.signal.channels_buffers for summarie in X_val]

    y_train = [summarie.has_anomaly() for summarie in X_train]
    y_val = [summarie.has_anomaly() for summarie in X_val]

    X_train_raw = np.array(X_train_raw)
    X_val_raw = np.array(X_val_raw)
    y_train = np.array(y_train)
    y_val = np.array(y_val)

    return X_train_raw, X_val_raw, y_train, y_val
