CREATE TABLE summary_info
(
    record_name VARCHAR(20),
    file_name VARCHAR(20),
    start_time TIME,
    end_time TIME,
    nr_seizures INTEGER,
    start_seizure INTEGER,
    end_seizure INTEGER,
    nr_channels INTEGER,
    ds_channels VARCHAR(500),
    PRIMARY KEY (file_name)
);