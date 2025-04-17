#!/bin/env python

import sys
import os
import json
import boto3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
envS3_ENDPOINT = os.getenv("S3_ENDPOINT")
envS3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
envS3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
envS3_REGION = os.getenv("S3_REGION")

client = boto3.client("s3",
                endpoint_url=envS3_ENDPOINT,
                aws_access_key_id=envS3_ACCESS_KEY,
                aws_secret_access_key=envS3_SECRET_KEY,
                region_name=envS3_REGION)
bucket = 'cid'

def upload(srcfile:str, s3path:str, dstname:str=None, throwex:bool=True):
    if not dstname:
        dstname = os.path.basename(srcfile)
    if s3path.endswith('/'):
        dstname = s3path + dstname
    else:
        dstname = s3path + '/' + dstname
    if throwex:
        client.upload_file(srcfile, bucket, dstname)
    else:
        try:
            client.upload_file(srcfile, bucket, dstname)
        except BaseException as ex:
            return (False, ex)
    return (True, dstname)

def download(srcfile:str, localpath:str=".", dstname:str=None, throwex:bool=True):
    if not dstname:
        dstname = os.path.basename(srcfile)
    if localpath.endswith('/'):
        dstname = localpath + dstname
    else:
        dstname = localpath + '/' + dstname
    if throwex:
        client.download_file(Bucket=bucket, Key=srcfile, Filename=dstname)
    else:
        try:
            client.download_file(Bucket=bucket, Key=srcfile, Filename=dstname)
        except BaseException as ex:
            return (False, ex)
    return (True, dstname)

def store(data, s3path:str, dstname:str, throwex:bool=True, encoding:str="utf-8"):
    dstname = s3path + '/' + dstname
    if type(data) == dict:
        data = bytes(json.dumps(data), encoding=encoding)
    elif type(data) == str:
        data = bytes(data, encoding=encoding)
    elif type(data) != bytes:
        raise ValueError(f"Invalid type '{type(data).__name__}'")
    if throwex:
        client.put_object(Body=bytes(data), Bucket=bucket, Key=dstname)
    else:
        try:
            client.put_object(Body=data, Bucket=bucket, Key=dstname)
        except BaseException as ex:
            return (False, ex)
    return (True, dstname)

if __name__ == "__main__":
    print("Not to be run directly", file=sys.stderr)
    exit(1)