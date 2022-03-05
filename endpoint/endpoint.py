from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from typing import Any
import pymysql
import boto3, sys, os

from schemas import DataSchema, Response
from config import rds_settings

app = FastAPI()


def rds_insert(schema: DataSchema):
    print("Connecting to Database")
    db = pymysql.connect(
        host=rds_settings.RDS_URL,
        user=rds_settings.RDS_USER,
        password=rds_settings.RDS_PW,
        port=rds_settings.RDS_PORT,
        database=rds_settings.RDS_BDD,
    )

    with db.cursor() as cur:
        # Print all the tables from the database
        cur.execute('SHOW TABLES FROM dbName')
        for r in cur:
            print(r)
    try:
        return {"status": True, "message": ""}
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        print("Could not connect")
        return {"status": False, "message": e}


def s3_insert(file: bytes):
    print("S3")
    return


@app.post("/rds", name="data-app", response_model=Response)
def rds_endpoint(schema: DataSchema, ) -> Any:
    print("¨POST request for RDS")

    return rds_insert(schema)


@app.post("/s3", name="data-app", response_model=Response)
def s3_endpoint(file: bytes = File(...)) -> Any:
    print("¨POST request for S3")

    return s3_insert(file)
