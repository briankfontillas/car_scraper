from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
Quick way to see what cars are on the market!
'''

######function
def car_lookup():

    search = input('Search: ')

    return search

#######launch window
browser = webdriver.Chrome("C:\\Users\\brian\\OneDrive\\Desktop\\chromedriver.exe") #<----Different location for each user
browser.get('https://seattle.craigslist.org/d/cars-trucks/search/cta')

#######Search
search_engine = browser.find_element_by_id('query')

search_engine.click()
search_engine.send_keys(car_lookup())

browser.find_element_by_class_name('min').click()
min = input('Minimum cost: ')
browser.find_element_by_class_name('min').send_keys(min)

browser.find_element_by_class_name('max').click()
max = int(input('Maximum cost: '))
browser.find_element_by_class_name('max').send_keys(max)

search_engine.send_keys(Keys.ENTER)

######scraping
ads = browser.find_elements_by_class_name('hdrlnk')

for ad in ads:
    print('Ad Title: ' + ad.text)
