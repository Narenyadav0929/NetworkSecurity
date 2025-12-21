import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_ATLAS_URL")
# print(mongo_db_url)

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.pipeline.training_pipeline import TraningPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import Response, RedirectResponse
from uvicorn import run as app_run
import pandas as pd
import numpy as np
import pymongo
from networksecurity.utils.main_utils.utils import load_object


client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import (DATA_INGESTION_DATABASE_NAME , 
                                                        DATA_INGESTION_COLLECTION_NAME)

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train_route():
    try:
        traning_pipeline_config = TrainingPipelineConfig()

        traning_pipeline = TraningPipeline(training_pipeline_config=traning_pipeline_config)
        traning_pipeline.run_pipeline()
        return Response("Tranning is done")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
    if __name__ == "__main__":
        app_run(app,host="localhost",port=8000)