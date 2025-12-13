import os
import sys
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
from typing import List
from sklearn.model_selection import train_test_split
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TranningPipelineConfig


# loading enviroment variable
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_ATLAS_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def export_collection_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_clinet = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_clinet[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df.drop(columns=["_id"],axis=1,inplace=True)

            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_injetion(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

trainning_config = TranningPipelineConfig()
config = DataIngestionConfig(trainning_config)
obj = DataIngestion(config)
obj.export_collection_as_dataframe()