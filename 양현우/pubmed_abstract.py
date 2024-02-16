from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import time
import platform
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd



def get_titles(start_num, end_num, search_word, title_list, site_list):
# start_num ~ end_num 까지 크롤링
    while start_num <= end_num:
        url = ('https://pubmed.ncbi.nlm.nih.gov/?term={}&page={}'.format(search_word, start_num))
        req = requests.get(url)
        time.sleep(1)
        url1 = 'https://pubmed.ncbi.nlm.nih.gov'
        if req.ok: #정상적인 request 확인
            soup =BeautifulSoup(req.text, 'html.parser')
            news_titles = soup.find_all('a', {'class':'docsum-title'})
            for news in news_titles:
                print(news.text.strip())
                title_list.append(news.text.strip())
                site_list.append(url1+news.attrs['href'])
        start_num += 1
        print('title 개수:', len(title_list))
        print(title_list)
        print(site_list)

def get_abstract(site_list, abst_list):
    for a in site_list:
        print(a)
        req = requests.get(a)
        time.sleep(1)
        if req.ok: #정상적인 request 확인
            soup =BeautifulSoup(req.text, 'html.parser')
            try:
                abstract = soup.select_one('div#eng-abstract').text
            except:
                abstract = ''
            print(abstract)
            abst_list.append(abstract)


def make_wordcloud(title_list):
    text = ''.join(title_list)
    img_mask = np.array(Image.open('DNA.png'))
    STOPWORDS.add('big')
    STOPWORDS.add('data')
    STOPWORDS.add('analysis')
    STOPWORDS.add('using')
    STOPWORDS.add('based')
    STOPWORDS.add('research')
    STOPWORDS.add('application')
    STOPWORDS.add('model')
    STOPWORDS.add('artificial intelligence')
    STOPWORDS.add('machine learning')
    STOPWORDS.add('health')
    STOPWORDS.add('healthcare')


    print(type(STOPWORDS))
    wordcloud = WordCloud(width=400, height=400,
                          background_color='white', max_font_size=200,
                          stopwords=STOPWORDS,
                          repeat=True,
                          colormap='nipy_spectral', mask=img_mask).generate(text)

    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.show()

site_list = []
title_list = []
abst_list = []
get_titles(1,10,'covid', title_list, site_list)
make_wordcloud(title_list)

# get_abstract(site_list,abst_list)
# make_wordcloud(abst_list)
# dp = pd.DataFrame(title_list, columns=['논문 제목'])
# dp['사이트 링크'] = site_list
# dp['요약'] = abst_list
# dp.to_csv('big_data_thesis.csv',encoding='utf-8-sig')