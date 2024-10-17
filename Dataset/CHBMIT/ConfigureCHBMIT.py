import os
import re
from wfdb import io
from urllib.request import urlretrieve
from Database.DatabaseSummary import DatabaseSummary


def get_summary(part_code):
    url = "https://physionet.org/physiobank/database/chbmit/" + part_code + "/" + part_code + "-summary.txt"
    directory = "./data/CHBMIT/" + part_code + "/"
    filename = part_code + "-summary.txt"

    fullpath = os.path.join(directory, filename)

    if not os.path.exists(fullpath):
        os.makedirs(directory)
        urlretrieve(url, fullpath)


def get_edf_by_record(record, file):
    url = "https://physionet.org/physiobank/database/chbmit/" + record + "/" + file
    directory = "./data/CHBMIT/" + record + "/"
    filename = file

    fullpath = os.path.join(directory, filename)

    if not os.path.exists(fullpath):
        try:
            print(f"DOWNLOADING: {fullpath}")
            urlretrieve(url, fullpath)
            print(f"DOWNLOADING: {fullpath}")

        except:
            print(f"DOWNLOAD NOT POSSIBLE: {filename}")

    else:
        print(f"EXISTS: {fullpath}")


def get_summary_info(record):
    directory = "./data/CHBMIT/" + record + "/"
    filename = record + "-summary.txt"
    fullpath = os.path.join(directory, filename)

    with open(fullpath, encoding="UTF-8") as f:
        content = f.readlines()
        f.close()

    return content


def summary_info(content, record_name):

    database = DatabaseSummary()

    nr_channels = 0
    file_name = ""
    start_time = ""
    end_time = ""
    start_seizure = []
    end_seizure = []
    nr_seizures = ""
    ds_channels = []

    for line in content:

        if re.findall("Channel \\d+", line):
            nr_channels += 1
            channel = re.findall(line.split(": ")[1], line)[0].replace("\n", "")
            ds_channels.append(channel)

        elif re.findall("Channels changed", line):
            nr_channels = 0
            ds_channels.clear()

        elif re.findall("File Name", line):
            file_name = re.findall("\\w+_\\w+.\\.edf", line)[0]

        elif re.findall("File Start Time", line):
            start_time = re.findall("\\d+:\\d+:\\d+", line)[0]

        elif re.findall("File End Time", line):
            end_time = re.findall("\\d+:\\d+:\\d+", line)[0]

        elif re.findall("(Seizure \\d+ Start Time|Seizure Start Time)", line):
            seizure = re.findall("\\d+", line.split(": ")[1])[0].replace("\n", "")
            start_seizure.append(seizure)

        elif re.findall("(Seizure \\d+ End Time|Seizure End Time)", line):
            seizure = re.findall("\\d+", line.split(": ")[1])[0].replace("\n", "")
            end_seizure.append(seizure)

        elif re.findall("Number of Seizures in File", line):
            nr_seizures = re.findall("\\d+", line)[0]

        else:
            if file_name != "" and int(nr_seizures) > 0:
                directory = "data/CHBMIT/" + record_name + "/"
                fullpath = os.path.join(directory, file_name)

                get_edf_by_record(record_name, file_name)

                if os.path.exists(fullpath):
                    if database.summary_by_name(file_name) is None:
                        print(f"INSERTING: {file_name}")
                        database.insert_sumarry_data("CHBMIT", record_name, file_name, start_time, end_time, int(nr_seizures), ",".join(start_seizure), ",".join(end_seizure), nr_channels, ",".join(ds_channels), "epilepsy")
                    else:
                        print(f"INSERTED: {file_name}")

                file_name = ""
                start_time = ""
                end_time = ""
                start_seizure.clear()
                end_seizure.clear()
                nr_seizures = ""


def download_and_process():
    records_list = io.get_record_list("chbmit", records="all")
    part_codes = sorted(list(set([record.split("/")[0] for record in records_list])))

    for part_code in part_codes:
        print(f"PROCESSING: {part_code}")
        get_summary(part_code)
        record_context = get_summary_info(part_code)
        summary_info(record_context, part_code)
