import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
import bcrypt
import string
import jwt
import datetime
from flask_cors import CORS

try:
    # Verbindungsaufbau zur Datenbank
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='PasswordManager'
    )
    print("Connected Succesfully")
except Error as e:
    print("Error on MYSQL connection", e)

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(stored_hash, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

def is_valid_password(password: str) -> bool:

    has_letter = any(char.isalpha() for char in password)  # Mindestens ein Buchstabe 
    has_digit = any(char.isdigit() for char in password)   # Mindestens eine Zahl
    has_special = any(char in string.punctuation for char in password)  # Sonderzeichen
    
    if len(password) < 8: return 0
    if has_letter != True: return 0
    if has_digit != True: return 0
    if has_special != True: return 0 

    return 1

def getUser(username):
    query = """
    Select * From users
    where Login_Name = %s
    """
    cursor = connection.cursor()
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    cursor.close()
    return result

def saveUser(last_name, first_name, password, login_name):
    hashed_password = hash_password(password)
    query="""
    Insert into users (last_name, first_name, master_password_hash, login_name)
    Value(%s, %s, %s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(query, (last_name, first_name, hashed_password, login_name))
    connection.commit()
    cursor.close()
    return 1

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # Allows all origens to access the API
secret_key = "password_manager"

def create_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")
    

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    last_name = data.get("last_name")
    first_name = data.get("first_name")
    password = data.get("password")
    login_name = data.get("login_name")
    
    if is_valid_password(password) and getUser(login_name) == []: 
        saveUser(last_name, first_name, password, login_name)
        return "Successfully Created User", 201

    elif is_valid_password != True: return "Check Passwords Requirements", 400

@app.route("/login", methods=["POST"])
def login_user():
    try:
        data = request.get_json()
        login_name = data.get("login_name")
        password = data.get("password")
        user = getUser(login_name)
        Hased_password = user[0][3]
        if check_password(Hased_password.encode('utf-8'), password):
            return "Login Successful", 200
        return "Login Failed", 400
    except:
        return "Login Failed", 400

if __name__ == "__main__":
        app.run(debug=True)