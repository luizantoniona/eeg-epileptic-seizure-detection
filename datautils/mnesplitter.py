import model.summarymodel as sm
import numpy as np
import datautils.summarysplitter as splitter
    
def time_data_splitter(summaries: list[sm.SummaryModel]):
    X_train, X_val, y_train, y_val = splitter.summaries_data_splitter(summaries)

    X_train = np.array(X_train)
    X_val = np.array(X_val)
    y_train = np.array(y_train)
    y_val = np.array(y_val)

    return X_train, X_val, y_train, y_val