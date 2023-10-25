import model.summarymodel as sm

def model_from_tuple(summary_tupple) -> sm.SummaryModel:

    summary_start_times = []
    summary_end_times = []

    if summary_tupple['start_seizure'] != '':
        summary_start_times = [int(x) for x in str(summary_tupple['start_seizure']).split(',')]

    if summary_tupple['end_seizure'] != '':
        summary_end_times = [int(x) for x in str(summary_tupple['end_seizure']).split(',')]

    model = sm.SummaryModel (
        summary_tupple['record_name'],
        summary_tupple['file_name'],
        summary_tupple['start_time'],
        summary_tupple['end_time'],
        summary_tupple['nr_seizures'],
        summary_start_times,
        summary_end_times,
        summary_tupple['nr_channels'],
        str(summary_tupple['ds_channels']).split(',')
    )

    return model