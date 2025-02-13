import mysql.connector
from mysql.connector import Error

try:
    # Verbindungsaufbau zur Datenbank
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='passwordmanager'
    )
    print("Connected Succesfully")
except Error as e:
    print("Error on MYSQL connection", e)