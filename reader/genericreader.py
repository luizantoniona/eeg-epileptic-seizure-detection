import mne

def read_generic(summary_model):
    return mne.io.read_raw("./data/" + summary_model.record_name + "/" + summary_model.file_name)