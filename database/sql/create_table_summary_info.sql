CREATE TABLE summary_info
(
    record_name VARCHAR(20),
    file_name VARCHAR(20),
    start_time TIME,
    end_time TIME,
    nr_seizures INTEGER,
    start_seizure VARCHAR(500),
    end_seizure VARCHAR(500),
    nr_channels INTEGER,
    ds_channels VARCHAR(500),
    PRIMARY KEY (file_name)
);