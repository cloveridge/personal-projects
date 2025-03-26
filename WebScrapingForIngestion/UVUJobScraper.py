# import beautifulsoup as bs
import selenium
from selenium.webdriver import Edge,EdgeOptions,EdgeService,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup as bs
from time import sleep



def ScrapeJobs_UVU(site,search):
    search_url = f'{site['Website']}&keywords={search.replace(' ','%20')}'

    driver_options = EdgeOptions()
    #driver_options.add_argument("--headless")  # Run in headless mode (no UI)
    driver_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection

    driver_service = EdgeService()

    driver = Edge(service=driver_service,options=driver_options)
    driver.get(search_url)
    
    sleep(1)

    job_list_container = driver.find_element(By.CLASS_NAME, "unstyled.search-results-listing-container.job-listing-container")
    job_list = job_list_container.find_elements(By.TAG_NAME, "li")
    
    for element in job_list:
        print(element)
    


if __name__ == '__main__':
    searches = ['data engineer','data warehouse','data']
    sites_to_search = [
        {'Company':'UVU','Website':'https://www.schooljobs.com/careers/uvu?sort=PostingDate%7CDescending','Function':ScrapeJobs_UVU}
    ]
    jobs_list = []

    for site in sites_to_search:
        for search in searches:
            site['Function'](site,search)