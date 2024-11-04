from flask import Flask, jsonify


app = Flask(__name__)

# Route for checking if a number is prime
@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

# Example function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Route for fetching airport information
@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    # Replace this with actual database lookup logic
    if icao_code.upper() == "EFHK":
        airport_info = {"ICAO": "EFHK", "Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"}
    else:
        return jsonify({"error": "Airport not found"}), 404
    return jsonify(airport_info)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
