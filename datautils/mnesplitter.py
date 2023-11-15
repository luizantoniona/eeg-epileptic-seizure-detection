import model.summarymodel as sm
import datautils.summarysplitter as splitter
import numpy as np
    
def time_data_splitter(summaries: list[sm.SummaryModel]):
    X_train, X_val, y_train, y_val = splitter.summaries_data_splitter(summaries)

    X_train_time_data = np.array([summary.signal.get_time_data()[0] for summary in X_train])
    X_val_time_data = np.array([summary.signal.get_time_data()[0] for summary in X_val])

    return X_train_raw, X_val_raw, y_train, y_val