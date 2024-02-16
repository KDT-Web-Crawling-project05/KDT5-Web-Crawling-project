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


def make_wordcloud(title_list):
    text = ''.join(title_list)
    img_mask = np.array(Image.open('DNA.png'))
    STOPWORDS.add('big')
    STOPWORDS.add('data')
    STOPWORDS.add('analysis')
    STOPWORDS.add('using')
    STOPWORDS.add('based')
    STOPWORDS.add('research')
    STOPWORDS.add('method')
    STOPWORDS.add('model')
    STOPWORDS.add('use')
    STOPWORDS.add('system')
    STOPWORDS.add('methods')
    STOPWORDS.add('result')
    STOPWORDS.add('results')
    STOPWORDS.add('used')
    STOPWORDS.add('information')
    STOPWORDS.add('provide')
    STOPWORDS.add('study')
    STOPWORDS.add('application')
    STOPWORDS.add('different')
    STOPWORDS.add('algorithm')
    STOPWORDS.add('development')
    STOPWORDS.add('database')
    STOPWORDS.add('studies')
    STOPWORDS.add('clinical')
    STOPWORDS.add('dataset')
    STOPWORDS.add('set')
    STOPWORDS.add('time')
    STOPWORDS.add('new')
    STOPWORDS.add('tool')
    STOPWORDS.add('technology')
    STOPWORDS.add('developments')
    STOPWORDS.add('area')
    STOPWORDS.add('machine learning')
    STOPWORDS.add('tools')
    STOPWORDS.add('number')
    STOPWORDS.add('two')
    STOPWORDS.add('technique')
    STOPWORDS.add('approach')
    STOPWORDS.add('framework')
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

data2 = pd.read_csv('big_data_thesis.csv', index_col=0)
data2.index = range(1,4001)
title_list = data2['논문 제목'].to_list()
abst_list = data2['요약'].dropna().tolist()

print(type(abst_list))
make_wordcloud(abst_list)


list = ['a','b','c', 'd']

print(''.join(list))

