import database.databaseutils as db
import model.summarymodelconverter as converter
import reader.reader as reader

def load_summaries():
    all_summaries = []

    db.connect()
    db_objects = db.all_summary()

    for db_object in db_objects:
        all_summaries.append(converter.model_from_tuple( db_object ))

    return all_summaries

def load_mne_objects():

    all_mne_object = []

    for summary in load_summaries():
        all_mne_object.append(reader.mne_edf(summary))

    return all_mne_object

def time_objects():
    all_time_objects = []

    for mne_object in load_mne_objects():
        all_time_objects.append(mne_object.get_data())

    return all_time_objects

def psd_objects():
    all_psd_objects = []

    for mne_object in load_mne_objects():
        all_psd_objects.append(mne_object.compute_psd().get_data())

    return all_psd_objects

def spec_objects():
    all_spec_objects = []

    ##TODO: Calcular o espectro de potência de cada time_object

    return all_spec_objects