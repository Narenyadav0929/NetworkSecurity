from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file

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

