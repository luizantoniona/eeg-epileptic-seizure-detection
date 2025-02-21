import concurrent.futures
import Object.SummaryConverter as Converter
from Database.DatabaseSummary import DatabaseSummary
from Dataset.DatasetTypeEnum import DatasetTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Object.Summary import Summary


class Loader:
    """
    Class: Loader
    This class provides functions to load and process summary data from a database, as well as generate various types of data and segmented data from the loaded summaries.
    """

    @staticmethod
    def load_summaries(dataset_type: DatasetTypeEnum) -> list[Summary]:
        """
        Load summary data from the database and convert it into a list of Summary objects.
        """
        summaries = []

        database = DatabaseSummary()
        db_objects = database.summaries(dataset_type)

        for db_object in db_objects:
            summaries.append(Converter.model_from_tuple(db_object))

        return summaries

    @staticmethod
    def load_anomalous_summaries(dataset_type: DatasetTypeEnum) -> list[Summary]:
        """
        Load anomalous summary data from the database and convert it into Summary objects.
        """
        summaries = []

        database = DatabaseSummary()
        db_objects = database.summaries_with_anomaly(dataset_type.name)

        for db_object in db_objects:
            summaries.append(Converter.model_from_tuple(db_object))

        return summaries

    @staticmethod
    def load_summary(dataset_type: DatasetTypeEnum, file_name: str = "") -> list[Summary]:
        """
        Load summary data from the database and convert it into Summary object.
        """
        summaries = []

        database = DatabaseSummary()
        db_object = database.summary_by_name(dataset_type.name, file_name)

        summaries.append(Converter.model_from_tuple(db_object))

        return summaries

    @staticmethod
    def load_segmented_data(summaries: list[Summary], signal_type: SignalTypeEnum, window_length: int, full_file=False, max_workers=8) -> None:
        """
        Generate segmented data of specified type for a list of Summary objects.

        Args:
        - summaries (list[Summary]): List of Summary objects to process.
        - signal_type (SignalTypeEnum): Type of signal data to generate ("Time", "PSD", "Spectrogram").
        - window_length (int): Length of the time window wich the data will be segmented.
        - full_file (bool, optional): Whether to generate full file data. Defaults to False.
        """

        def generate(summary: Summary):
            print(f"GENERATING:{signal_type.name} WINDOW:{str(window_length)} FILE:{summary.file_name}")

            if full_file:
                summary.generate_segmented_data_full_file(signal_type=signal_type, window_length=window_length)
            else:
                summary.generate_segmented_data_around_seizures(signal_type=signal_type, window_length=window_length)

        if not summaries:
            print("NO SUMMARIES. EXITING.")
            return

        if window_length <= 0:
            print("INVALID WINDOW LENGTH. EXITING.")
            return

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(generate, summaries)
