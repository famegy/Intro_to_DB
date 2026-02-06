import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kayole@1960"
    )
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(" Database 'alx_book_store' created successfully!")

except Error as e:
    print("An error occured when connecting to the MySQL server:", e)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed.")