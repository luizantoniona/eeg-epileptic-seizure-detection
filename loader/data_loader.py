"""
Module: data_loader

This module provides functions to load and process summary data from a database, as well as generate various types of data and segmented data from the loaded summaries.
"""

import database.database_utils as db
import model.summary_model_converter as converter
from model.summary_model import SummaryModel
import concurrent.futures

def load_summaries() -> list[SummaryModel]:
    """
    Load summary data from the database and convert it into a list of SummaryModel objects.
    """
    summaries = []

    db.connect()
    db_objects = db.summaries()

    for db_object in db_objects:
        summaries.append(converter.model_from_tuple(db_object))

    return summaries

def load_anomalous_summaries() -> list[SummaryModel]:
    """
    Load anomalous summary data from the database and convert it into SummaryModel objects.
    """
    summaries = []

    db.connect()
    db_objects = db.summaries_with_anomaly()

    for db_object in db_objects:
        summaries.append(converter.model_from_tuple(db_object))

    return summaries

def load_mne_data(summaries: list[SummaryModel]) -> None:
    """
    Generate MNE data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_mne()

def load_time_segmented_data(summaries: list[SummaryModel], full_file = False) -> None:
    """
    Generate segmented time data for a list of SummaryModel objects.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if(full_file):
            executor.map(lambda summary: summary.generate_segmented_time_data_full_file(), summaries)
        else:
            executor.map(lambda summary: summary.generate_segmented_time_data(), summaries)

def load_freq_data(summaries: list[SummaryModel]) -> None:
    """
    Generate frequency data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.signal.generate_freq_data()

def load_freq_segmented_data(summaries: list[SummaryModel], full_file = False) -> None:
    """
    Generate segmented frequency data for a list of SummaryModel objects.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if(full_file):
            executor.map(lambda summary: summary.generate_segmented_freq_data_full_file(), summaries)
        else:
            executor.map(lambda summary: summary.generate_segmented_freq_data(), summaries)
