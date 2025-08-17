#!/usr/bin/python3
"""
Script to create the database 'alx_book_store' in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user and password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close connection safely
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
