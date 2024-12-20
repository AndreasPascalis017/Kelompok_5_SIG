from flask import Flask, render_template, request, jsonify
import json
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/geojson', methods=['POST'])
def geojson():
    try:
        # Ambil data lat dan lon dari request
        user_lat = request.json.get('user_lat')
        user_lon = request.json.get('user_lon')

        # Membaca file GeoJSON
        with open('sebaran-sma-bandar-lampung.geojson') as f:
            data = json.load(f)

        max_distance = 10  # Maksimum jarak dalam kilometer

        for feature in data['features']:
            if 'SMA Negeri' in feature['properties']['poi_name']:  # Filter hanya SMA Negeri
                school_lat = feature['geometry']['coordinates'][1]
                school_lon = feature['geometry']['coordinates'][0]

                # Hitung jarak dengan Geopy
                distance = geodesic((user_lat, user_lon), (school_lat, school_lon)).kilometers

                if distance <= max_distance:
                    distance_score = max(0, 1 - (distance / max_distance))
                    # Menambahkan data jarak dan probabilitas
                    feature['properties']['distance'] = round(distance, 2)
                    feature['properties']['probability'] = round((distance_score) * 100, 2)

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
