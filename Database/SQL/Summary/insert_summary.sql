INSERT INTO summary_info
(
    record_name,
    file_name,
    start_time,
    end_time,
    nr_occurrence,
    start_occurrence,
    end_occurrence,
    nr_channels,
    ds_channels,
    disease_type
)
VALUES (
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
);