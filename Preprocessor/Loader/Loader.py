"""
Module: Loader

This module provides functions to load and process summary data from a database, as well as generate various types of data and segmented data from the loaded summaries.
"""

import concurrent.futures
import Object.SummaryConverter as Converter
from Database.DatabaseSummary import DatabaseSummary
from Object.Summary import Summary

def load_summaries() -> list[Summary]:
    """
    Load summary data from the database and convert it into a list of Summary objects.
    """
    summaries = []

    database = DatabaseSummary()
    db_objects = database.summaries()

    for db_object in db_objects:
        summaries.append(Converter.model_from_tuple(db_object))

    return summaries

def load_anomalous_summaries() -> list[Summary]:
    """
    Load anomalous summary data from the database and convert it into Summary objects.
    """
    summaries = []

    database = DatabaseSummary()
    db_objects = database.summaries_with_anomaly()

    for db_object in db_objects:
        summaries.append(Converter.model_from_tuple(db_object))

    return summaries

def load_segmented_data(summaries: list[Summary], signal_type: str, time_window: int, full_file=False) -> None:
    """
    Generate segmented data of specified type for a list of Summary objects.

    Args:
    - summaries (list[Summary]): List of Summary objects to process.
    - signal_type (str): Type of signal data to generate ("time", "PSD", "spectrogram").
    - full_file (bool, optional): Whether to generate full file data. Defaults to False.
    """
    def generate(summary: Summary):
        if full_file:
            summary.generate_segmented_data_full_file(signal_type=signal_type, time_window=time_window)
        else:
            summary.generate_segmented_data(signal_type=signal_type, time_window=time_window)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(generate, summaries)