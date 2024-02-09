"""
Module: data_loader

This module provides functions to load and process summary data from a database, as well as generate various types of data and segmented data from the loaded summaries.
"""

import database.database_utils as db
import model.summary_model_converter as converter
import model.summary_model as sm

def load_summaries() -> list[sm.SummaryModel]:
    """
    Load summary data from the database and convert it into a list of SummaryModel objects.
    """
    summaries = []

    db.connect()
    db_objects = db.summaries()

    for db_object in db_objects:
        summaries.append(converter.model_from_tuple(db_object))

    return summaries

def load_anomalous_summaries() -> list[sm.SummaryModel]:
    """
    Load anomalous summary data from the database and convert it into SummaryModel objects.
    """
    summaries = []

    db.connect()
    db_objects = db.summaries_with_anomaly()

    for db_object in db_objects:
        summaries.append(converter.model_from_tuple(db_object))

    return summaries

def load_mne_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate MNE data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_mne()

def load_freq_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate MNE frequency data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.signal.generate_freq_data()

def load_time_freq_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate time-frequency data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.signal.generate_time_freq_data()

def load_time_segmented_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate segmented time data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_segmented_time_data()

def load_freq_segmented_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate segmented frequency data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_segmented_freq_data()

def load_time_freq_segmented_data(summaries: list[sm.SummaryModel]) -> None:
    """
    Generate segmented time-frequency data for a list of SummaryModel objects.
    """
    for summary in summaries:
        summary.generate_segmented_time_freq_data()
