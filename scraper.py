from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

CHROMEDRIVER_PATH = "./chromedriver/chromedriver.exe"

def run_scraper(search_query, num_pages=1):
    options = Options()
    options.add_argument("--headless")
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    base_url = f"https://www.shine.com/job-search/{search_query.replace(' ', '-').lower()}-jobs"
    jobs = []

    def extract_detail_info(detail_url):
        try:
            driver.get(detail_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobdetailsNova_jdJobTxt__ND51u"))
            )
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, "html.parser")

            description_elem = soup.find("pre", class_="jobdetailsNova_jdJobTxt__ND51u")
            salary_elem = soup.find("ul", class_="jobdetailsNova_jdKeyHighlightList__nAcEl")
            salary = ""
            if salary_elem:
                salary_items = salary_elem.find_all('li')
                if len(salary_items) >= 3:
                    salary = salary_items[2].get_text(strip=True)

            skills_elem = soup.find("ul", class_="jdSkillsNova_jdSkillsCardTopList__GU29K")
            skills = [li.get_text(strip=True) for li in skills_elem.find_all("li")] if skills_elem else []

            location_elem = soup.find("div", class_="jobdetailsNova_jDLocationTxt___U_GN")
            location = location_elem.get_text(strip=True) if location_elem else ""

            return {
                "Description": description_elem.get_text(strip=True) if description_elem else "",
                "Salary": salary,
                "Skills": ", ".join(skills),
                "Location": location
            }
        except:
            return {"Description": "", "Salary": "", "Skills": "", "Location": ""}

    for page in range(1, num_pages + 1):
        driver.get(f"{base_url}?page={page}")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobCardNova_bigCard__W2xn3"))
            )
        except:
            continue

        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_cards = soup.find_all("div", class_="jobCardNova_bigCard__W2xn3")

        for card in job_cards:
            title_elem = card.find("p", class_="jobCardNova_bigCardTopTitleHeading__Rj2sC")
            link_elem = card.find("a", href=True)
            company_elem = card.find("span", class_="jobCardNova_bigCardTopTitleName__M_W_m")
            experience_elem = card.find("span", class_="jobCardNova_bigCardCenterListExp__KTSEc")
            createdDate_elem = card.find("span", class_="jobApplyBtnNova_days__yODJj")

            if title_elem and company_elem and link_elem:
                job_url = "https://www.shine.com" + link_elem['href']
                details = extract_detail_info(job_url)
                jobs.append({
                    "Job Title": title_elem.get_text(strip=True),
                    "Company": company_elem.get_text(strip=True),
                    "Experience": experience_elem.get_text(strip=True) if experience_elem else "",
                    "Created Date": createdDate_elem.get_text(strip=True) if createdDate_elem else "",
                    "Location": details["Location"],
                    "Salary": details["Salary"],
                    "Skills": details["Skills"],
                    "Description": details["Description"],
                    "Link": job_url
                })
                time.sleep(1)

    driver.quit()

    df = pd.DataFrame(jobs)
    os.makedirs("scraped_jobs", exist_ok=True)
    csv_path = f"scraped_jobs/{search_query.replace(' ', '_')}_jobs.csv"
    df.to_csv(csv_path, index=False)
    return jobs, csv_path