from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image
import koreanize_matplotlib


def make_wordcloud(title_list, stopwords, word_count):
    okt = Okt()
    sentences_tag = []
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)

    noun_adj_list = []
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective'] and len(word) > 1:
                noun_adj_list.append(word)

    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)

    tag_dict = dict(tags)
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)

    if platform.system() == 'Windows':
        path = path = r'C:\Windows\Fonts\malgun.ttf'
    elif platform.system() == 'Darwin':
        path = r'/System/Library/Fonts/AppleGothic'
    else:
        path = r'/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'

    img_mask = np.array(Image.open('DATA/pngwing.com.png'))
    wordcloud = WordCloud(font_path=path, width=800, height=800,
                          background_color='white', max_font_size=200,
                          repeat=True, colormap='brg', mask=img_mask)

    cloud = wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.title("빅데이터 관련 학술논문", y=-0.1)
    plt.show()


if __name__ == '__main__':
    title_list = []
    stopwords = ['빅데이터', '활용', '방안', '분야', '사례', '분석', '현황', '중심',
                 '대한', '한국', '활성화', '데이터', '기반', '동향', '인식', '이닝',
                 '이용', '기법', '통한', '워드', '시대', '의미', '적용', '과제', '국내']

    with open('./DATA/title_list.txt', 'r', encoding='utf-8') as f:
        title_list = eval(f.read())

    make_wordcloud(title_list, stopwords, 200)
