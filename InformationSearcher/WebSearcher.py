'''
Simple script to read in source data for things to search on the web.
'''
import os
import random
from time import sleep

SEARCH_FILE = 'InformationSearcher\BingList.txt'
SEARCHED_FILE = 'InformationSearcher\BingList.txt'
EDGE_PATH = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
BASE_URL = 'https://www.bing.com/search'
QUALIFIER = '&form=QBLH&PC=U531'

def SearchWeb(search):
    search_local = str(search).replace(' ','+')
    os.system(f'"{EDGE_PATH}" -url {BASE_URL}?q={search_local}{QUALIFIER}')

def GetSearches(topX):
    '''
    Pops X searches from the source file, loads them into the archive file, and returns them
    '''
    searches = []
    modified_full_list = []

    with open(SEARCH_FILE, 'r') as full_list, open(SEARCHED_FILE,'a') as used_list:
        modified_full_list = list(full_list.readlines())
        random.shuffle(modified_full_list)
        while len(searches) < topX:
            search = modified_full_list.pop(0)
            used_list.write(search)
            searches.append(str(search).replace(',',''))
    with open(SEARCH_FILE,'w') as full_list:
        full_list.writelines(modified_full_list)
    return searches

if __name__ == '__main__':
    cooldown_time = 15 # minutes to not overload servers
    batch_size = 3 # Number of searches between cooldowns to respect servers
    number_searches = batch_size * 10

    searches = GetSearches(topX=number_searches)
    batch_count = batch_size
    while searches:
        if batch_count < 1:
            sleep(cooldown_time * 60) 
        else:
            sleep(int(random.random() * 60))
        
        SearchWeb(searches.pop(0))

        if batch_count == 1 or not searches:
            batch_count = batch_size
            # Kill search engine
            os.system("taskkill /IM msedge.exe")
        else:
            batch_count -= 1