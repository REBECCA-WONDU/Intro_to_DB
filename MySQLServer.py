#!/usr/bin/python3
"""
Script to create the database 'alx_book_store' in MySQL server
without using SELECT or SHOW, and with proper exception handling.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Attempt to connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # replace with your MySQL root password
        )

        cursor = connection.cursor()
        # Create database safely without SELECT/SHOW
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle MySQL-specific errors
        print("MySQL Error:", err)

    except Exception as e:
        # Handle any other unexpected errors
        print("Unexpected Error:", e)

    finally:
        # Ensure the connection is closed
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    create_database()
