
import database.databaseutils as db
import reader.reader as reader
import model.summarymodelconverter as converter
import pyedflib

db.connect()

db_object = db.summary_by_name('chb01_03.edf')
summary_model = converter.model_from_tuple( db_object )

edf_file = reader.mne_edf(summary_model)

print(edf_file.annotations)