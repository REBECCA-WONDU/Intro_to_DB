#!/usr/bin/python3
"""Script to create the alx_book_store database in MySQL"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Function to create the alx_book_store database"""
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",    # Update with your credentials
            password=""     # Update with your password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database (won't fail if exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        # Specific handling for MySQL errors
        print(f"MySQL Error occurred: {e}")
    except Exception as e:
        # General exception handling
        print(f"An unexpected error occurred: {e}")
    finally:
        # Cleanup in finally block
        try:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()
        except Exception as cleanup_error:
            print(f"Error during cleanup: {cleanup_error}")

if __name__ == "__main__":
    create_database()