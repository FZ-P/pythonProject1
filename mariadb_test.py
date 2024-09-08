import mariadb

# Initialize the connection variable
connection = None

try:
    # Establish the connection
    connection = mariadb.connect(
        user='prianka',
        password='your_password_here',  # Ensure this matches the actual password
        host='127.0.0.1',
        port=3306,
        database='flight_game'
    )
    print("Connected to MariaDB")

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT DATABASE();")

    # Fetch the result
    db_name = cursor.fetchone()
    print(f"You're connected to database: {db_name[0]}")

except mariadb.Error as e:
    print(f"Error: {e}")

finally:
    if connection:
        connection.close()
        print("MariaDB connection is closed")

