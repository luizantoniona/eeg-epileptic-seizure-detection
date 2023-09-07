import model.summarymodel as summary

def model_from_tuple(summary_tupple):
    model = summary.SummaryModel
    model.record_name = summary_tupple['record_name']
    model.file_name = summary_tupple['file_name']
    model.start_time = summary_tupple['start_time']
    model.end_time = summary_tupple['end_time']
    model.nr_seizures = summary_tupple['nr_seizures']
    model.start_seizure = summary_tupple['start_seizure']
    model.end_seizure = summary_tupple['end_seizure']
    model.nr_channels = summary_tupple['nr_channels']
    model.ds_channels = summary_tupple['ds_channels']

    return model