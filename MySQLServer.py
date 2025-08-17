#!/usr/bin/python3
"""
Script to create the database 'alx_book_store' in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Change this to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database safely; no SELECT or SHOW used
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # Handle MySQL connection errors
        print("Error while connecting to MySQL:", err)

    except Exception as e:
        # Handle any other unexpected errors
        print("Unexpected error:", e)

    finally:
        # Ensure connection closes safely
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
