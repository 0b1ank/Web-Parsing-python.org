import requests
from bs4 import BeautifulSoup

URL = "https://www.python.org/jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("ol", class_="list-recent-jobs")

job_cards = results.find_all("li")

for job_card in job_cards:
    title_element = job_card.find("a")
    company_element = job_card.find("span", class_="listing-company-name")
    location_element = job_card.find("span", class_="listing-location")
    company_name = list(company_element.stripped_strings)[-1]
    print(title_element.text.strip())
    print(company_name.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[0]["href"]
    print(f"Apply here: https://www.python.org{link_url}\n")
    print()
    print()
