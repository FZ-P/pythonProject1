import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host='localhost',  # Replace with your database host
        user='your_username',  # Replace with your database username
        password='your_password',  # Replace with your database password
        database='your_database'  # Replace with your database name
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")

        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")

        # Example: Fetch all rows from a table
        cursor.execute("SELECT * FROM your_table")  # Replace with your table name
        rows = cursor.fetchall()

        print("Fetching all rows from your_table:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
