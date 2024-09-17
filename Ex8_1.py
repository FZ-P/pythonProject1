import mysql.connector


def get_airport_by_icao(icao_code):
    try:
        # Establish the connection to the MySQL database
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='your_username',
            password='your_password',
            database='flight_game'
        )

        cursor = conn.cursor()

        # SQL query to fetch the airport name and location (town) by ICAO code
        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print(f"Airport Name: {result[0]}, Location: {result[1]}")
        else:
            print("No airport found with this ICAO code.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()
# Ask the user for the ICAO code
icao_code = input("Enter the ICAO code of the airport: ").upper()
get_airport_by_icao(icao_code)
