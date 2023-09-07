import model.summarymodel as summary

def model_from_tuple(summary_tupple):
    model = summary.SummaryModel (
        summary_tupple['record_name'],
        summary_tupple['file_name'],
        summary_tupple['start_time'],
        summary_tupple['end_time'],
        summary_tupple['nr_seizures'],
        summary_tupple['start_seizure'],
        summary_tupple['end_seizure'],
        summary_tupple['nr_channels'],
        summary_tupple['ds_channels']
    )

    return model