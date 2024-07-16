# This script is used as a lambda function in AWS
# to get information from a DynamoDB noSQL about
# simple pizza items.

import json
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    # Initialize DynamoDB resources with boto3
    dynamodb = boto3.resource("dynamodb")

    # Creates a table resource object that represents
    # the dynamodb table
    table = dynamodb.Table("Pizza")

    # Extracting the key from the event
    pathParams = event.get("pathParameters")
    item_id = pathParams["id"]
    if not item_id:
        return {"statusCode": 400, "body": json.dumps("Error: id not provided!")}

    # Fetching the item from the DynamoDB with 'Pizza' table
    try:
        response = table.get_item(Key={"id": item_id})

        if "Item" not in response:
            return {"statusCode": 404, "body": json.dumps("Item not found.")}

        return {"statusCode": 200, "body": json.dumps(response["Item"])}

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error retrieving item: {str(e)}"),
        }
