from Dataset.DatasetTypeEnum import DatasetTypeEnum

def configure(dataset_type: DatasetTypeEnum):

    match dataset_type:
        case DatasetTypeEnum.CHBMIT:
            #TODO
            return
        
        case _:
            print("Not Mapped")
