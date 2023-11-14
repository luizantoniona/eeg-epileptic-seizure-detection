import model.summarymodel as sm
import datautils.summarysplitter as splitter
    
def time_data_splitter(summaries: list[sm.SummaryModel]):
    X_train, X_val, y_train, y_val = splitter.summaries_data_splitter(summaries)

    return X_train, X_val, y_train, y_val