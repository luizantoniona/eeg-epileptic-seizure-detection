SELECT * FROM summary_info 
    WHERE nr_occurrence > 0
    AND record_name != 'chb24'
    AND file_name != 'chb12_27.edf'
    AND file_name != 'chb12_28.edf'
    AND file_name != 'chb12_29.edf'
    AND dataset_name = ?;
