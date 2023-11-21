import database.databaseutils as db
import model.summarymodelconverter as converter
import model.summarymodel as sm

def load_summaries() -> list[sm.SummaryModel]:
    all_summaries = []

    db.connect()
    db_objects = db.all_summary()

    for db_object in db_objects:
        all_summaries.append(converter.model_from_tuple( db_object ))

    return all_summaries

def load_mne_data(summaries: list[sm.SummaryModel]) -> None:
    for summary in summaries:
        summary.generate_mne()

def load_segmented_data(summaries: list[sm.SummaryModel]) -> None:
    for summary in summaries:
        summary.generate_segmented_data()

def load_raw_data(summaries: list[sm.SummaryModel]) -> None:
    for summary in summaries:
        try:
            summary.generate_signal()
        except:
            summaries.remove(summary)