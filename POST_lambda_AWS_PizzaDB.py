# This script is used as a lambda function in AWS
# to post/put information inside a DynamoDB noSQL.
# The input has to be JSON in the format of:

#   {
#       "id": "<string>",
#       "size": "<string>,
#       "topping": "<string>
#   }

import json
import boto3
# from boto3.dynamodb.conditions import Key

# Get the service resource
dynamodb = boto3.resource("dynamodb")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table("Pizza")


def lambda_handler(event, context):

    try:
        # Parse the request body
        body = json.loads(event["body"])
        item_id = body["id"]
        item_size = body["size"]
        item_top = body["topping"]
        # item_id = '5'
        # item_size = 'medium'
        # item_top = 'mushrooms'

        table.put_item(Item={"id": item_id, "size": item_size, "topping": item_top})

        # Return a success response
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Item successfully inserted"}),
        }

    except Exception as e:
        # Return an error response
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
