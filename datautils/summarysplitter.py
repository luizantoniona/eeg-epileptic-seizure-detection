import model.summarymodel as sm
import numpy as np
from sklearn.model_selection import train_test_split

def summaries_data_splitter(summaries: list[sm.SummaryModel]) -> (list[sm.SummaryModel], list[sm.SummaryModel], np.array, np.array) :
    X_train, X_val = train_test_split(summaries, test_size=0.2, random_state=42)

    y_train = [summary.has_anomaly() for summary in X_train]
    y_val = [summary.has_anomaly() for summary in X_val]

    y_train = np.array( y_train)
    y_val = np.array(y_val)

    return X_train, X_val, y_train, y_val