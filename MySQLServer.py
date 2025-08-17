#!/usr/bin/python3
"""Script to create the alx_book_store database in MySQL"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Function to create the alx_book_store database"""
    try:
        # Establish connection to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username if different
            password=""   # Replace with your MySQL password if set
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()