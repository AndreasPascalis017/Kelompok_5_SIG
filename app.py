from flask import Flask, render_template, request, jsonify
import psycopg2
import json

app = Flask(__name__)

# Koneksi ke database PostgreSQL dengan nama 'tubes_sig'
def get_db_connection():
    conn = psycopg2.connect(
        dbname='tubes_sig',  # Nama database
        user='ddima',  # Ganti dengan username PostgreSQL Anda
        password='200345',  # Ganti dengan password PostgreSQL Anda
        host='localhost',  # Host database
        port='5432'  # Port default PostgreSQL
    )
    return conn

# Endpoint untuk mengirimkan GeoJSON ke frontend
@app.route('/geojson')
def geojson():
    with open('sebaran-sma-bandar-lampung.geojson') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')  # Halaman utama aplikasi

if __name__ == '__main__':
    app.run(debug=True)
