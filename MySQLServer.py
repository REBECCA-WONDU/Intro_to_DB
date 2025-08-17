#!/usr/bin/python3
"""
Script to create the database 'alx_book_store' in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database safely (no SELECT/SHOW used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # ✅ Explicit exception handling
        print("Error while connecting to MySQL:", err)

    except Exception as e:
        # ✅ Catch any other unexpected errors
        print("Unexpected error:", e)

    finally:
        # ✅ Ensure connection closes even if error occurs
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
