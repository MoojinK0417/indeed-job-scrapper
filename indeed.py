import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://ca.indeed.com/jobs?q=python&l=Ontario&radius=100&limit={LIMIT}&vjk=369437712218a654"


def extract_indeed_pages():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]  # put -1 in the list is bringing last of list value]

    return max_page


def extract_job(html):

    title = html.find("h2", {"class": "jobTitle"}).find("a").find("span").string
    company = html.find("div", {"class": "companyInfo"}).find("span").string
    location = html.find("div", {"class": "companyLocation"}).string
    link = html.find("a")["data-jk"]

   
    return {'title':title, 'company': company, 'locations': location, 'link': f"https://ca.indeed.com/viewjob?jk={link}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):

        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={0*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "job_seen_beacon"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs

def get_jobs():
    last_page = extract_indeed_pages()
    jobs = extract_jobs(last_page)
    return jobs


