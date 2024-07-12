from datetime import datetime, timedelta
from Object.Summary import Summary

def time_to_timedelta(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

def model_from_tuple(db_object) -> Summary:

    summary_tupple = dict(db_object)

    summary_start_times = []
    summary_end_times = []

    if summary_tupple['start_occurrence'] != '':
        summary_start_times = [int(x) for x in str(summary_tupple['start_occurrence']).split(',')]

    if summary_tupple['end_occurrence'] != '':
        summary_end_times = [int(x) for x in str(summary_tupple['end_occurrence']).split(',')]

    model = Summary (
        summary_tupple['record_name'],
        summary_tupple['file_name'],
        time_to_timedelta(summary_tupple['start_time']),
        time_to_timedelta(summary_tupple['end_time']),
        summary_tupple['nr_occurrence'],
        summary_start_times,
        summary_end_times,
        summary_tupple['nr_channels'],
        str(summary_tupple['ds_channels']).split(','),
        summary_tupple['disease_type']
    )

    return model