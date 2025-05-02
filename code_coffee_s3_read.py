import boto3
import csv
import io

AWS_ACCESS_KEY = 'xxx'
AWS_SECRET_KEY = 'xxx'
AWS_BUCKET_NAME = 'codecoffeawsprimer'


def get_file():
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    response = s3_client.get_object(Bucket=AWS_BUCKET_NAME, Key='code_coffee.csv')
    csv_content = response['Body'].read().decode('utf-8')
    csv_file = io.StringIO(csv_content)
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)


if __name__ == '__main__':
    get_file()
