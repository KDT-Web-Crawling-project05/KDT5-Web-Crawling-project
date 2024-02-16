import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from konlpy.tag  import Okt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from PIL import Image

thesisDF = pd.read_csv('./thesis_info.csv')
print(thesisDF.head())