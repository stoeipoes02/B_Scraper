# scraping from https://realpython.github.io/fake-jobs/
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")                   # find by id
job_elements = results.find_all("div", class_="card-content")# find by HTML class name

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())  
    print(company_element.text.strip()) # only prints the text 
    print(location_element.text.strip()) # strips text of unnessecary whitespaces
    print()