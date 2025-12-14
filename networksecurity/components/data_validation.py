from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file


import sys, os
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


class DataValidation:
    def __init__(self,data_injetion_artifact:DataIngestionArtifact,
                  data_validation_config:DataValidationConfig):
        
        try:
            self.data_injetion_artifact = data_injetion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        
        except Exception as e:
            raise(NetworkSecurityException(e, sys))
        
    @staticmethod
    def read_file(file_path)-> pd.DataFrame:
        """
        Reads a CSV file and returns a pandas DataFrame
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        


    def validate_number_of_columns(self,dataframe : pd.DataFrame) -> bool:
        try:
            ymal_file = self._schema_config
            number_of_columns = len(ymal_file['columns'])

            logging.info(f"Required number of columns:{number_of_columns}")
            logging.info(f"Data frame has columns:{len(dataframe.columns)}")

            if not number_of_columns == len(dataframe.columns):
                return False
            
            for index_ in range(len(ymal_file['numerical_columns'])):
                if ymal_file['numerical_columns'][index_] == dataframe.columns.to_list()[index_]:
                    pass 
                else:
                    print('header name are different')
                    return False
            
            logging.info("all the columns name pass the schema")
            return True
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def validate_all_numerical_columns(self,dataframe : pd.DataFrame) -> bool:
        try:
            return all(pd.api.types.is_numeric_dtype(dtype) for dtype in dataframe.dtypes)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def detect_dataser_drift(self, base_df:pd.DataFrame, current_df:pd.DataFrame,threshold=0.05) -> bool:
        try:
            staus = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1,d2)
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    staus = False

                report.update({column:{
                    "p_value":float(is_same_dist.pvalue),
                    "drift_status":is_found
                    
                    }})
            drift_report_file_path = self.data_validation_config.drift_report_file_path

            #Create directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)

        except Exception as e:
            raise NetworkSecurityException(e,sys)

            



    def initiate_data_validation(self):
        try:
            train_file_path = self.data_injetion_artifact.train_file_path
            test_file_path = self.data_injetion_artifact.test_file_path

            # read train and test data
            train_dataframe = DataValidation.read_file(train_file_path)
            test_dataframe = DataValidation.read_file(test_file_path)

            #validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                print(f"Train dataframe does not contain all columns.\n")
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                print(f"Test dataframe does not contain all columns.\n")

            #validate Numeric columns
            status = self.validate_all_numerical_columns(train_dataframe)
            if not status:
                error_message = 'All the columns of tranning dataset are not numerical'
                print(error_message)
            status =  self.validate_all_numerical_columns(test_dataframe)
            if not status:
                error_message = 'All the columns of test dataset are not numerical'
                print(error_message)


            # lets check data drift
            status = self.detect_dataser_drift(base_df=train_dataframe, current_df=test_dataframe)

            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path, exist_ok=True)

            # saving valid train and test data
            train_dataframe.to_csv(path_or_buf=self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_dataframe.to_csv(path_or_buf=self.data_validation_config.valid_test_file_path, header=True, index=False)

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path= self.data_validation_config.valid_train_file_path,
                valid_test_file_path= self.data_validation_config.valid_test_file_path,
                invalid_test_file_path=None,
                invalid_train_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )
            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)


