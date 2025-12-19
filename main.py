from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
import sys

if __name__ == "__main__":
    try:
        tranningpipelineconfig = TrainingPipelineConfig()
        logging.info('Data Injetion is started')
        datainjestionconfig = DataIngestionConfig(tranningpipelineconfig)
        datainjestion = DataIngestion(datainjestionconfig)
        dataartifact = datainjestion.initiate_data_injetion()
        logging.info('Data Injetion is completed and Data validation is started')
        datavalidationconfig = DataValidationConfig(tranningpipelineconfig)
        datavalidation = DataValidation(data_injetion_artifact=dataartifact,data_validation_config=datavalidationconfig)
        data_validation_artfact=datavalidation.initiate_data_validation()
        logging.info('Data validation is completed')
        logging.info('Initiate data transformation')
        data_transformation_config = DataTransformationConfig(tranningpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artfact,
                                                  data_transformation_config= data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info('Data transformation completed')

        print(data_transformation)



    except Exception as e:
        raise(NetworkSecurityException(e, sys))
