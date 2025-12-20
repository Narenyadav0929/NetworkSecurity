import os
import sys
from networksecurity.constant.training_pipeline import SAVE_MODEL_DIR, MODEL_TRAINER_TRAINED_MODEL_NAME
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkModel:
    def __init__(self,processor,model):
        try:
            self.processor = processor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def predict(self,x):
        try:
            X_trasform = self.processor.transform(x)
            y_hat = self.model.predict(X_trasform)
            return y_hat

        except Exception as e:
            raise NetworkSecurityException(e,sys)