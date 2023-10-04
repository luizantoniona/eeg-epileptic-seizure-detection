import database.databaseutils as db
import model.summarymodelconverter as converter
import reader.reader as reader

def load_summaries():
    all_summaries = []

    db.connect()
    db_objects = db.all_summary()

    for db_object in db_objects:
        all_summaries.append(converter.model_from_tuple( db_object ))

    print(len(all_summaries))

    return all_summaries

def load_mne_objects():

    all_mne_object = []

    for summary in load_summaries():
        all_mne_object.append(reader.mne_edf(summary))

    print(len(all_mne_object))

    return all_mne_object

def time_objects():
    return ""

def psd_objects():
    return ""

def spec_objects():
    return ""