SELECT * FROM metrics_info
    WHERE model_name = ?
    AND model_data_domain = ?
    AND model_window_length = ?
    AND accuracy = (SELECT MAX(accuracy) FROM metrics_info);
