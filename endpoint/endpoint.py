from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from typing import Any
import mysql.connector
import boto3, sys, os

from schemas import DataSchema, Response
from config import rds_settings

app = FastAPI()

def connect():
    return mysql.connector.connect(
            host=rds_settings.RDS_URL,
            user=rds_settings.RDS_USER,
            passwd=rds_settings.RDS_PW,
            port=rds_settings.RDS_PORT,
            database=rds_settings.RDS_BDD,
            ssl_ca='')

def rds_insert(schema: DataSchema):
    print("Connecting to Database")
    return

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""SELECT now()""")
        query_results = cur.fetchall()
        print(query_results)
        return {"status": True, "message": ""}
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        return {"status": False, "message": e}

def s3_insert(file: UploadFile = File(...)):
    print("S3")
    return

@app.post("/rds", name="data-app", response_model=Response)
def rds_endpoint(schema: DataSchema,) -> Any:
    print("¨POST request for RDS")

    return rds_insert(schema)


@app.post("/s3", name="data-app", response_model=Response)
def s3_endpoint(file: UploadFile) -> Any:
    print("¨POST request for S3")

    return s3_insert(file)
