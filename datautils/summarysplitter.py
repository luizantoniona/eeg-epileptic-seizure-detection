import model.summarymodel as sm
from sklearn.model_selection import train_test_split

def summaries_data_splitter(summaries: list[sm.SummaryModel]):
    X_train, X_val = train_test_split(summaries, test_size=0.2, random_state=42)

    y_train = [summary.has_anomaly() for summary in X_train]
    y_val = [summary.has_anomaly() for summary in X_val]

    return X_train, X_val, y_train, y_val