# scraping from https://realpython.github.io/fake-jobs/
import requests
from bs4 import BeautifulSoup
import mariadb
import sys

try:
  conn = mariadb.connect(
    user='exampleuser',
    password='kick',
    host='localhost',
    database='example'
  )

except mariadb.error as e:
  print(f'error connecting to mariadb platform: {e}')
  sys.exit(1)

cur = conn.cursor()




URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")                   # find by id
job_elements = results.find_all("div", class_="card-content")# find by HTML class name

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    title = title_element.text.strip()
    company = company_element.text.strip()
    location = location_element.text.strip()

    # Insert job information into the database
    try:
        cur.execute("INSERT INTO jobs (title, company, location) VALUES (?, ?, ?)", (title, company, location))
        conn.commit()
        print(f"Job inserted: {title}, {company}, {location}")
    except mariadb.Error as e:
        print(f"Error inserting job: {e}")

# Close the database connection
conn.close()
