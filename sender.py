import json
import boto3
import sys

cli = boto3.client("sqs", region_name='us-east-1')


def send_message(url, attr, body, delay=0):
    cli.send_message(
        QueueUrl=url,
        DelaySeconds=0,
        MessageAttributes=attr,
        MessageBody=body,
    )


if __name__ == '__main__':
    output = {'message': sys.argv[1],
              'token': 'Bearer YOUR_LINE_NOTIFY_TOKEN', }
    send_message(
        url="YOUR_AWS_SQS_URL",
        attr={},
        body=json.dumps(output)
    )
