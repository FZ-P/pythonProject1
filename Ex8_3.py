import mysql.connector
from geopy.distance import geodesic


def get_coordinates_by_icao(icao_code):
    try:
        # Establish the connection to the MySQL database
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='your_username',
            password='your_password',
            database='flight_game'
        )

        cursor = conn.cursor()

        # SQL query to fetch the latitude and longitude of the airport by ICAO code
        query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            return (result[0], result[1])
        else:
            print(f"No coordinates found for airport with ICAO code {icao_code}.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        cursor.close()
        conn.close()


def calculate_distance_between_airports(icao1, icao2):
    coords1 = get_coordinates_by_icao(icao1)
    coords2 = get_coordinates_by_icao(icao2)

    if coords1 and coords2:
        # Calculate distance using geodesic function from geopy
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"The distance between {icao1} and {icao2} is {distance_km:.2f} km.")
    else:
        print("Unable to calculate the distance due to missing coordinates.")


# Ask the user for two ICAO codes
icao1 = input("Enter the ICAO code of the first airport: ").upper()
icao2 = input("Enter the ICAO code of the second airport: ").upper()

calculate_distance_between_airports(icao1, icao2)
