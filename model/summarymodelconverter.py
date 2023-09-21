import model.summarymodel as summary

def model_from_tuple(summary_tupple):
    model = summary.SummaryModel (
        summary_tupple['record_name'],
        summary_tupple['file_name'],
        summary_tupple['start_time'],
        summary_tupple['end_time'],
        summary_tupple['nr_seizures'],
        str(summary_tupple['start_seizure']).split(','),
        str(summary_tupple['end_seizure']).split(','),
        summary_tupple['nr_channels'],
        str(summary_tupple['ds_channels']).split(',')
    )

    return model