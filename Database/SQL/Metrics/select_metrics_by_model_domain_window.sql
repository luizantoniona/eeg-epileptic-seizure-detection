SELECT * FROM metrics_info
    WHERE model_name = ?
    AND model_data_domain = ?
    AND model_window_length = ?;
