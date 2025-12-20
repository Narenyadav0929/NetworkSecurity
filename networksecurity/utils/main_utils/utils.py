from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import yaml
import dill
import pickle
import os, sys
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise (NetworkSecurityException(e,sys))
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)



def save_numpy_array_data(file_path:str, array:np.array) -> None:
    """
    save numpy aarray to file
    """
    try:    
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    


def save_object(file_path: str, obj: object) -> None:
    try:    
        logging.info("Enter the save object method of main_utils class")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Exited the save_object method of main_utils class")
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

def load_object(file_path : str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f'file path {file_path} does not exist')
        with open(file_path, "rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    

def load_numpy_array_data(file_path : str) -> np.array:
    
    """
    Load numpy array from file_path : str
    and return np.array
    """
    try:
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e, sys)  from e
    


def evaluate_models(x_train, y_train, x_test, y_test, models : dict, params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            params = params[list(models.keys())[i]]

            gs = GridSearchCV(estimator=model, param_grid=params, cv = 3)
            gs.fit(x_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train, y_train)

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_r2_score = r2_score(y_true=y_train, y_pred=y_train_pred)
            test_model_score = r2_score(y_true=y_test, y_pred=y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            return report




    except Exception as e:
        raise NetworkSecurityException(e, sys)
    



