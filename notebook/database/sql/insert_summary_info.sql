INSERT INTO summary_info
(
    record_name,
    file_name,
    start_time,
    end_time,
    nr_seizures,
    start_seizure,
    end_seizure,
    nr_channels 
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
);