from flask import Flask, jsonify, send_file
from scraper import main
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🚓 TPS Crime Scraper is online. Visit /scrape to run it."

@app.route("/scrape")
def scrape():
    try:
        main(50)  # Scrape 50 articles
    except Exception as e:
        return jsonify({"error": f"Scraper failed: {str(e)}"}), 500

    if not os.path.exists("crime_data_final.xlsx"):
        return jsonify({"error": "No data file generated."}), 404

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
    return send_file(
        path,
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
