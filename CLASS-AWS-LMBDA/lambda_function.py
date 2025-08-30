import json

def lambda_handler(event, context):
    print("Lambda function has been invoked.")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }