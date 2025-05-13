from flask import Flask, render_template, request, send_file
from scraper import run_scraper

app = Flask(__name__)
latest_csv = ""

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", jobs=None)

@app.route("/scrape", methods=["POST"])
def scrape():
    global latest_csv
    search_query = request.form["query"]
    num_pages = int(request.form["pages"])
    jobs, csv_path = run_scraper(search_query, num_pages)
    latest_csv = csv_path
    return render_template("index.html", jobs=jobs)

@app.route("/download")
def download_csv():
    return send_file(latest_csv, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)