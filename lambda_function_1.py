import boto3
import json

ACCESS_HEADERS = {
                "Access-Control-Allow-Headers" : "Content-Type",
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"}

def lambda_handler(event, context):
    print("Hello CodePipeline!")
    return {
        'statusCode': 200,
        'headers': ACCESS_HEADERS,
        'body': json.dumps('Hello From LF1 in CodePipeline')
    }