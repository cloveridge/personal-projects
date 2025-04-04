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

    with Edge(service=driver_service,options=driver_options) as driver:
        driver.get(search_url)
        
        sleep(1)

        job_list_container = driver.find_element(By.CLASS_NAME, "unstyled.search-results-listing-container.job-listing-container")
        job_list = job_list_container.find_elements(By.XPATH, '//ul[contains(@class, "unstyled") and contains(@class, "search-results-listing-container") and contains(@class, "job-listing-container")]/li')
        #parent_id = job_list[0].parent.id
        jobs = []

        for element in job_list:
            title = element.find_element(By.CLASS_NAME,'item-details-link').text
            job_metadata = element.find_element(By.CLASS_NAME,'list-meta').find_elements(By.TAG_NAME,'li')
            job_type = job_metadata[0].text
            job_category = job_metadata[1].text
            job_description_top = element.find_element(By.CLASS_NAME,'list-entry').find_elements(By.TAG_NAME,'span')
            job_description = f'{job_description_top[0].text} {job_description_top[1].text}'
            job_window = element.find_element(By.CLASS_NAME,'list-published')
            job_start = job_window.find_element(By.TAG_NAME,'span').find_element(By.TAG_NAME,'span').text
            job_close = job_window.find_elements(By.TAG_NAME,'span')[3].text
            #print(element)

            jobs.append({'title':title  
                        ,'job_type':job_type
                        ,'job_category':job_category
                        ,'job_description':job_description
                        ,'job_start':job_start
                        ,'job_close':job_close
                        ,'job_salary':0})
    return jobs
            #print(element.find_element())

#def SendJobDigest(job_list):
    


if __name__ == '__main__':
    searches = ['data engineer','data warehouse','data']
    sites_to_search = [
        {'Company':'UVU','Website':'https://www.schooljobs.com/careers/uvu?sort=PostingDate%7CDescending','Function':ScrapeJobs_UVU}
    ]
    job_titles_list = []
    jobs_list = []

    for site in sites_to_search:
        for search in searches:
            job_results = site['Function'](site,search)
            for job in job_results:
                if job['title'] not in job_titles_list:
                    job_titles_list.append(job['title'])
                    jobs_list.append(job)
    
    for job in jobs_list:
        print(job['title'])