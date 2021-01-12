## Import libraries
from bs4 import BeautifulSoup
import pandas as pd
import glob
#import os 
from multiprocessing import Pool

## Function for getting trail review from html file
def html_to_csv(trail_html):
    trail_name = trail_html.split('/')[-1][:-5]
    print(trail_name)
    
    star_class_name = 'MuiRating-root default-module__rating___1k45X MuiRating-sizeLarge MuiRating-readOnly'
    date_class_name = 'styles-module__dateTrailDetails___3qgZC xlate-none'
    user_class_name = 'styles-module__nameTrailDetails___3L6cM'
    text_class_name = 'reviewBody'

    user_name=[]
    stars=[]
    dates=[]
    review_texts=[]
    trail = []
    
    soup = BeautifulSoup(open(trail_html), "html.parser")
    review_div=soup.find_all('div',{'itemprop':'review'})


    for i in range(len(review_div)):
        try:
            name = review_div[i].find_all('div',{'class':user_class_name})[1].text
        except:
            name = None

        try:
            star = review_div[i].find("span", {"class": star_class_name})['aria-label']
        except:
            star = None

        try:
            date = review_div[i].find("span", {"class": date_class_name}).text
        except:
            date = None       

        try:
            review_text = review_div[i].find('p',{'itemprop':text_class_name}).text
        except:
            review_text = None

        user_name.append(name)
        stars.append(star)
        dates.append(date)
        review_texts.append(review_text)
        trail.append(trail_name)


    df = pd.DataFrame({'user_name':user_name, 'stars': stars, 'date': dates, 'review_text': review_texts, 'trail': trail})
    csv_name = '/Users/eunheelim/Capstone3/csv/CA/' + trail_name + '.csv'
    df.to_csv(csv_name)

## Specify fold containing html files
filepath =  '/Users/eunheelim/Capstone3/html/CA/*.html'

## For parallel processing across all trails html files 
def main():
    pool = Pool()
    pool.map(html_to_csv, glob.glob(filepath))


if __name__ == "__main__":
    main()    