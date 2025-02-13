CREATE DATABASE PasswordManager;
USE PasswordManager;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    master_password_hash TEXT NOT NULL,
    login_name VARCHAR(10) NOT NULL
);

CREATE TABLE passwords (
    password_id INT PRIMARY KEY AUTO_INCREMENT,
    account_name VARCHAR(255) NOT NULL,
    encrypted_password TEXT NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);