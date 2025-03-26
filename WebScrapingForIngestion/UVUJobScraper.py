# import beautifulsoup as bs
import selenium
from selenium.webdriver import Edge,EdgeOptions,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup as bs



def ScrapeJobs_UVU(site,search):
    search_url = f'{site['Website']}?&keywords={search.replace(' ','%20')}'
    print(search_url)
    
    driver = Edge
    driver_options = EdgeOptions()
    driver_options.add_argument("--headless")  # Run in headless mode (no UI)
    driver_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
    
    driver = driver()



if __name__ == '__main__':
    searches = ['data engineer','data warehouse','data']
    sites_to_search = [
        {'Company':'UVU','Website':'https://www.schooljobs.com/careers/uvu','Function':ScrapeJobs_UVU}
    ]
    jobs_list = []

    for site in sites_to_search:
        for search in searches:
            site['Function'](site,search)