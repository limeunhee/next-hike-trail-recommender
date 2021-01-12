import requests
from requests import get
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import glob
import os 
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



# urls = 
    
def html_for_state(trail_url):
    print(trail_url)
    trail_name = trail_url.split('/')[-1][:-1]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/Users/eunheelim/Capstone1/chromedriver', options=chrome_options)
    driver.get(trail_url)
    page_num = 0
    a_prev=0
    
    while True:
        try:
            driver.find_element_by_css_selector('button.styles-module__button___1nuva ').click()
            time.sleep(1)
            if page_num %10 ==0:
                html = driver.page_source.encode('utf-8')
                results = urlopen(trail_url)
                soup=BeautifulSoup(html, 'html.parser')
                class_name='styles-module__showing___14AKF'
                div=soup.find_all('div',{'class':class_name})
                a = div[0].text  #Shows # of reviews showing out of total reviews
                if a == a_prev:
                    print('Ended', trail_name, page_num)
                    break
                elif a!= a_prev:
                    a_prev = a
                print(page_num, div[0].text, trail_name)
            page_num += 1
        except:
            print('Ended', trail_name, page_num)
            break

    html = driver.page_source.encode('utf-8')    
    soup = BeautifulSoup(html, "lxml")
    
    filename = '/Users/eunheelim/Capstone3/html/CA/'+ trail_name +'.html'
    with open(filename, 'w') as file:
        file.write(str(soup))
    print('Saved: ', filename)  
    return html
    
def main():
    pool = Pool()
    pool.map(html_for_state, urls)


if __name__ == "__main__":
    main()    