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

def load_time_segmented_data(summaries: list[Summary], full_file = False) -> None:
    """
    Generate segmented time data for a list of Summary objects.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if(full_file):
            executor.map(lambda summary: summary.generate_segmented_data_full_file(signal_type = "time"), summaries)
        else:
            executor.map(lambda summary: summary.generate_segmented_data(signal_type = "time"), summaries)

def load_psd_segmented_data(summaries: list[Summary], full_file = False) -> None:
    """
    Generate segmented PSD data for a list of Summary objects.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if(full_file):
            executor.map(lambda summary: summary.generate_segmented_data_full_file(signal_type = "PSD"), summaries)
        else:
            executor.map(lambda summary: summary.generate_segmented_data(signal_type = "PSD"), summaries)
