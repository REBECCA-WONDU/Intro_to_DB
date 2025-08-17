#!/usr/bin/python3
"""
Script to create the database 'alx_book_store' in MySQL server
without using any SELECT or SHOW statements, and with exception handling.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # replace with your MySQL root password
        )

        cursor = connection.cursor()
        # Create database safely
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # Handle MySQL connection errors
        print("MySQL Error:", err)

    except Exception as e:
        # Handle other unexpected errors
        print("Unexpected Error:", e)

    finally:
        # Ensure connection is closed properly
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
