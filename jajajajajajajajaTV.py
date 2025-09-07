# app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    markers = [
        {"lat": 35.6895, "lng": 139.6917, "img": "/static/tokyo.png", "name": "東京"},
        {"lat": 34.6937, "lng": 135.5023, "img": "/static/osaka.png", "name": "大阪"},
        {"lat": 43.0667, "lng": 141.3500, "img": "/static/sapporo.png", "name": "札幌"}
    ]
    return render_template ("MAPPU.html")

if __name__ == '__main__':
    app.run(debug=True)