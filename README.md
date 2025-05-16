# 💼 Shine.com Job Scraper Web App

A Flask-based web application that scrapes job listings from [Shine.com](https://www.shine.com) for a given search keyword. Easily search and download jobs by role or technology (e.g., "Data Engineer") with a clean, responsive UI.

![demo](https://github.com/user-attachments/assets/50c05f76-e27d-45dc-a9c2-477f9d62989b)

---

## 🚀 Features

- 🔍 Search jobs by keyword and number of pages
- 📄 Scrape detailed job data (title, company, experience, location, salary, skills, and description)
- 📊 Clean, responsive UI with loading spinner and results table
- 💾 Download scraped results as CSV
- 🌐 Host-ready for platforms like Replit and Railway

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Selenium, BeautifulSoup
- **Frontend**: HTML, Bootstrap, Jinja2
- **Others**: Pandas, ChromeDriver

---

## 🖥️ How It Works

1. Enter a search term (e.g., `"Data Engineer"`) and number of pages to scrape.
2. Click **Scrape Jobs**.
3. Wait for the spinner to finish.
4. View the results in a table.
5. Click **Download CSV** to export data.

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.8+
- Google Chrome or Chromium
- ChromeDriver (matching your browser version)

### 📥 Setup Locally

```bash
git clone https://github.com/HimanshuBelhekar/shine-job-scraper-app.git
cd shine-job-scraper-app
pip install -r requirements.txt
```

### ▶️ Run the App

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000/`.

---

## 📁 Project Structure

```
shine-job-scraper-app/
│
├── app.py                  # Main Flask app
├── scraper.py              # Scraping logic using Selenium & BeautifulSoup
├── templates/
│   └── index.html          # Web UI (Jinja2 + Bootstrap)
├── chromedriver/
│   └── chromedriver.exe    # Chromedriver
├── scraped_jobs/
│   └── <job>_jobs.csv      # CSV files uploaded here
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## 📸 Screenshots

| 🧾 Form UI | ⏳ Loading Spinner | 📊 Results Table |
|-----------|------------------|------------------|
| ![](screenshots/form.png) | ![](screenshots/spinner.png) | ![](screenshots/results.png) |

---

## 📎 Sample CSV Output

```csv
Job Title, Company, Experience, Location, Salary, Skills, Description, Link
Data Engineer, ABC Corp, 3-5 Years, Bangalore, ₹10L–₹15L, Python, SQL, Snowflake, ..., https://www.shine.com/...
```

---

## 👤 Author

**Himanshu Belhekar**  
[LinkedIn](https://www.linkedin.com/in/himanshu-belhekar/) • [GitHub](https://github.com/HimanshuBelhekar)

---

## 🌟 Star this repo if you find it useful!