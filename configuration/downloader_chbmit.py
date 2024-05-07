"""
Module: dowloader_chbmit

- Packages needed: 
    - requests
    - wfdb
"""

import os
import wfdb 
from urllib.request import urlretrieve

def get_summary( part_code ):
    url = "https://physionet.org/physiobank/database/chbmit/" + part_code + '/' + part_code + '-summary.txt'
    directory = "./data/" + part_code + '/'
    filename = part_code + "-summary.txt"

    fullpath = os.path.join( directory, filename )

    if not os.path.exists( fullpath ):
        os.makedirs( directory )
        urlretrieve( url, fullpath )
    else:
        print(part_code + ": Já existe")

def get_edf_by_record(record, file):
    url = "https://physionet.org/physiobank/database/chbmit/" + record + '/' + file
    directory = "./data/" + record + '/'
    filename = file

    fullpath = os.path.join( directory, filename )

    if not os.path.exists( fullpath ):
        try:
            urlretrieve( url, fullpath )
            print(fullpath + ": Baixado!")
        except:
            print( filename + ": Não foi possivel, verificar")
    
    else:
        print(fullpath + ": Já existe!")

def download():

    dbs = wfdb.get_dbs()
    records_list = wfdb.io.get_record_list('chbmit', records='all')

    part_codes = sorted(list(set([record.split('/')[0] for record in records_list])))
    edf_files = sorted(list(set([record.split('/')[1] for record in records_list])))

    for part_code in part_codes:
        get_summary( part_code )

    for record in part_codes:
        files_by_record = list( filter( lambda file: record + '_' in file, edf_files ) )
        for file in files_by_record:
            get_edf_by_record( record, file )
