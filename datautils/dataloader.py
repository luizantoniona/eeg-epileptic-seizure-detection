import database.databaseutils as db
import model.summarymodelconverter as converter
import model.summarymodel as sm

def load_summaries() -> list[sm.SummaryModel]:
    """
    Load summary data from the database and convert it into a list of SummaryModel objects.
    """
    summaries = []

    db.connect()
    db_objects = db.summaries()

    for db_object in db_objects:
        summaries.append(converter.model_from_tuple( db_object ))

    return summaries

def load_anomalous_summaries() -> list[sm.SummaryModel]:
    """
    Load anomalous summary data from the database and convert it into SummaryModel objects.
    """
    summaries = []

    db.connect()
    db_objects = db.summaries_with_anomaly()

    for db_object in db_objects:
        summaries.append(converter.model_from_tuple( db_object ))

    return summaries

def load_mne_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate MNE data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_mne()

def load_segmented_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate segmented data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_segmented_data()

def load_raw_data(summaries: list[sm.SummaryModel]) -> None:
    for summary in summaries:
        try:
            summary.generate_signal()
        except:
            summaries.remove(summary)