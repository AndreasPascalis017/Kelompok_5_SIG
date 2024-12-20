from flask import Flask, render_template, request, jsonify
import json
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/geojson')
def geojson():
    try:
        with open('sebaran-sma-bandar-lampung.geojson') as f:
            data = json.load(f)

        user_lat = -5.397  # Koordinat rumah user, bisa diganti dengan data dinamis
        user_lon = 105.268
        max_distance = 10  # Maksimum jarak dalam kilometer

        for feature in data['features']:
            if 'SMA Negeri' in feature['properties']['poi_name']:  # Filter hanya SMA Negeri
                school_lat = feature['geometry']['coordinates'][1]
                school_lon = feature['geometry']['coordinates'][0]

                # Hitung jarak dengan Geopy
                distance = geodesic((user_lat, user_lon), (school_lat, school_lon)).kilometers

                if distance <= max_distance:
                    distance_score = max(0, 1 - (distance / max_distance))
                    feature['properties']['distance'] = round(distance, 2)
                    feature['properties']['probability'] = round((distance_score) * 100, 2)

        return jsonify(data)

    except FileNotFoundError:
        return jsonify({"error": "File GeoJSON tidak ditemukan."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
