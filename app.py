from flask import Flask, jsonify, send_file
from scraper import main
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🚓 TPS Crime Scraper is online. Visit /scrape to run it."

@app.route("/scrape")
def scrape():
    main(50)  # Adjust number of articles here if needed
    if not os.path.exists("crime_data_final.xlsx"):
        return jsonify({"error": "No data found"}), 404
    return jsonify({
        "status": "✅ Scraping complete",
        "file": "crime_data_final.xlsx",
        "download_url": "/download"
    })

@app.route("/download")
def download():
    path = "crime_data_final.xlsx"
    if not os.path.exists(path):
        return jsonify({"error": "No file found. Run /scrape first."}), 404
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
