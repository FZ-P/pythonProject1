import mysql.connector


def get_airports_by_area_code(area_code):
    try:
        # Establish the connection to the MySQL database
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='your_username',
            password='your_password',
            database='flight_game'
        )

        cursor = conn.cursor()

        # SQL query to fetch airports by country code ordered by type
        query = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type"
        cursor.execute(query, (area_code,))

        # Fetch all results
        results = cursor.fetchall()

        if results:
            for row in results:
                print(f"Airport Type: {row[0]}, Count: {row[1]}")
        else:
            print(f"No airports found in {area_code}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()


# Ask the user for the area code (country code)
area_code = input("Enter the area code (e.g., FI for Finland): ").upper()
get_airports_by_area_code(area_code)
