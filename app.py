from flask import Flask, render_template, jsonify
import data

SQLITE_URI = 'sqlite:///data/data.sqlite3'


app = Flask(__name__)
data_manager = data.FlightData(SQLITE_URI)

@app.route('/<int:id>')
def flight_id(id):
    flight = data_manager.get_flight_by_id(id)
    flight_tuple = flight[0]
    flight_dict = {
        'id' : flight_tuple[0],
        'depature_airport' : flight_tuple[1],
        'arrival_airport' : flight_tuple[2],
        'airline' : flight_tuple[3],
        'depature_delay' : flight_tuple[4]
    }

    if flight is None:
        return '', 404
    return jsonify(flight_dict)
app.run()