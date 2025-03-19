# import beautifulsoup as bs

# class JobListing:
#     def __init__(self,site,title,salary,postdate,description):
#         self.site = site
#         self.title = title
#         self.salary = salary
#         self.postdate = postdate
#         self.description = description

def ScrapeJobs_UVU(site,search):
    pass

if __name__ == '__main__':
    pass
    searches = ['data engineer','data warehouse','data']
    sites_to_search = [
        {'Company':'UVU','Website':'https://www.schooljobs.com/careers/uvu'}
    ]
    jobs_list = []

    for site in sites_to_search:
        for search in searches:
            ScrapeJobs_UVU(site,search)