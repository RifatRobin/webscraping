from bs4 import *
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests

# bdjobs_text = requests.get("https://jobs.bdjobs.com/jobsearch.asp").text
session=HTMLSession()
bdjobs_text = session.get("https://jobs.bdjobs.com/jobsearch.asp").text
# soup = bs(bdjobs_text, 'lxml')
soup=bs(bdjobs_text, 'lxml')

django_jobs = soup.find_all("div", class_="col-md-12")

before_company_name=soup.find_all('div',class_='col-sm-12')

for bcname in before_company_name:
    company_name=bcname.find('div',class_='comp-name-text')
    print(company_name.text)
