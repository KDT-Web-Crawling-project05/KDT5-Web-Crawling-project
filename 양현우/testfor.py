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
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import os
from os import path

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
def make_wordcloud(title_list):
    text = ''.join(title_list)
    img_mask = np.array(Image.open(path.join(d, "DNA.png")))
    STOPWORDS.add('big')
    STOPWORDS.add('data')
    STOPWORDS.add('analysis')
    STOPWORDS.add('using')
    STOPWORDS.add('based')
    STOPWORDS.add('research')
    STOPWORDS.add('method')
    STOPWORDS.add('model')
    print(type(STOPWORDS))

    wc = WordCloud(width=400, height=400,
              background_color='white', max_font_size=200,
              stopwords=STOPWORDS,
              repeat=True,
              colormap='nipy_spectral', mask=img_mask)
    wordcloud = wc.generate(text)
    image_colors = ImageColorGenerator(img_mask)
    fig, axes = plt.subplots(1, 3)
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    axes[2].imshow(img_mask, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    plt.show()

data2 = pd.read_csv('big_data_thesis.csv', index_col=0)
data2.index = range(1,4001)
title_list = data2['논문 제목'].to_list()
abst_list = data2['요약'].dropna().tolist()

print(type(abst_list))
make_wordcloud(abst_list)


list = ['a','b','c', 'd']

print(''.join(list))

