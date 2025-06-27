from flask import Flask, jsonify, send_file
from tps_scraper import main
import os

app = Flask(__name__)

# ──────────────────────────────────────
# Root endpoint
# ──────────────────────────────────────
@app.route("/")
def home():
    return "🚓 TPS Crime Scraper tool is online. Visit /scrape to run it. "

# ──────────────────────────────────────
# Run the scraper
# ──────────────────────────────────────
@app.route("/scrape")
def scrape():
    try:
        main(50)  # Scrape the 50 most recent articles
    except Exception as e:
        return jsonify({"error": f"Scraper failed: {str(e)}"}), 500

    file_path = "crime_data_final.xlsx"
    if not os.path.exists(file_path):
        return jsonify({"error": "No data file generated."}), 404

    return jsonify({
        "status": "✅ Scraping complete",
        "file": os.path.basename(file_path),
        "download_url": "/download"
    })

# ──────────────────────────────────────
# Download the resulting Excel file
# ──────────────────────────────────────
@app.route("/download")
def download():
    file_path = "crime_data_final.xlsx"
    if not os.path.exists(file_path):
        return jsonify({"error": "No file found. Run /scrape first."}), 404
    return send_file(
        file_path,
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ──────────────────────────────────────
# Run the Flask app
# ──────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
