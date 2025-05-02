import boto3
import csv
import io
import mysql.connector

AWS_ACCESS_KEY = 'xxx'
AWS_SECRET_KEY = 'xxx'
AWS_BUCKET_NAME = 'codecoffeawsprimer'

db_host = "codecoffeedb2.cecft67dh8f0.us-east-1.rds.amazonaws.com"
db_user = "admin"
db_password = "codecoffeedbpwd"
db_name = "codecoffee"


def get_file():
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    response = s3_client.get_object(Bucket=AWS_BUCKET_NAME, Key='code_coffee.csv')
    csv_content = response['Body'].read().decode('utf-8')
    csv_file = io.StringIO(csv_content)
    csv_reader = csv.reader(csv_file)

    return csv_reader


def open_db():
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    if mydb.is_connected():
        print(f"Successfully connected to MySQL database: {db_name} on {db_host}")
        return mydb

    return False


def write_db(csv_file):
    db = open_db()
    mycursor = db.cursor()

    for row in csv_file:
        insert_query = f"INSERT INTO users (name, address, city, state, zip, phone) VALUES ('{row[0]}', '{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}')"
        mycursor.execute(insert_query)
        db.commit()

    mycursor.close()
    db.close()


def read_db():
    db = open_db()
    mycursor = db.cursor()
    query = "SELECT * FROM users"
    mycursor.execute(query)
    results = mycursor.fetchall()
    mycursor.close()
    db.close()

    return results


if __name__ == '__main__':
    csv_file = get_file()
    write_db(csv_file)

    data = read_db()

    for row in data:
        print(row)
