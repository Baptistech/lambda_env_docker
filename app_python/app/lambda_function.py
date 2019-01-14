import boto3
import os
import random

def handler():
    # table_name = os.environ['DYNAMODB_TABLE']
    table_name = "store_last_values"
    client = boto3.client("client", region_name='us-west-2')
    dynamodb = boto3.resource('dynamodb')
    id_to_store = "id_" + str(random.randint(1,10000))
    var_to_store = "var_" + str(random.randint(1,10000))
    table = dynamodb.Table(table_name)
    table.put_item(
       Item={
            'id': id_to_store,
            'var': var_to_store,
            'time': "23456789",
            'value': "89"
        }
    )

if __name__ == "__main__":
    handler()