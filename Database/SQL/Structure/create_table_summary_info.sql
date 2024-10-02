CREATE TABLE summary_info
(
    dataset_name VARCHAR(20),
    record_name VARCHAR(20),
    file_name VARCHAR(20),
    start_time TIME,
    end_time TIME,
    nr_occurrence INTEGER,
    start_occurrence VARCHAR(500),
    end_occurrence VARCHAR(500),
    nr_channels INTEGER,
    ds_channels VARCHAR(500),
    disease_type VARCHAR(20),
    PRIMARY KEY (file_name)
);
