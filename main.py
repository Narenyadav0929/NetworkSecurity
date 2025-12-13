from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import sys

if __name__ == "__main__":
    try:
        tranningpipelineconfig = TrainingPipelineConfig()
        datainjestionconfig = DataIngestionConfig(tranningpipelineconfig)
        datainjestion = DataIngestion(datainjestionconfig)
        dataartifact = datainjestion.initiate_data_injetion()
        print(dataartifact)
        
    
    except Exception as e:
        raise(NetworkSecurityException(e, sys))
