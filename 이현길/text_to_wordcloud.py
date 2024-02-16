from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image
import koreanize_matplotlib


def make_wordcloud(title_list, stopwords, word_count, mask_img, color_select):
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

    img_mask = np.array(Image.open(mask_img))
    wordcloud = WordCloud(font_path=path, width=800, height=800,
                          background_color='white', max_font_size=200,
                          repeat=True, colormap=color_select, mask=img_mask)

    cloud = wordcloud.generate_from_frequencies(tag_dict)
    return cloud



if __name__ == '__main__':
    title_list = []
    stopwords = ['빅데이터', '활용', '방안', '분야', '사례', '분석', '현황', '중심',
                 '대한', '한국', '활성화', '데이터', '기반', '동향', '인식', '이닝',
                 '이용', '기법', '통한', '워드', '시대', '의미', '적용', '과제', '국내']

    file_google = './DATA/title_list_google.txt'
    mask_googel = './DATA/black-document-icon.jpg'
    color_google = 'nipy_spectral'
    file_naver = './DATA/title_list_naver.txt'
    mask_naver = './DATA/pngwing.com.png'
    color_naver = 'brg'


    with open(file_google, 'r', encoding='utf-8') as f:
        title_list = eval(f.read())
    cloud_google = make_wordcloud(title_list, stopwords, 200, mask_googel, color_google)

    plt.figure(figsize=(12, 12))
    plt.axis('off')
    plt.imshow(cloud_google)
    plt.title("빅데이터 관련 학술논문", y=-0.1)
    plt.show()


    with open(file_naver, 'r', encoding='utf-8') as f:
        title_list = eval(f.read())
    cloud_naver = make_wordcloud(title_list, stopwords, 200, mask_naver, color_naver)

    plt.figure(figsize=(12, 12))
    plt.axis('off')
    plt.imshow(cloud_naver)
    plt.title("바이오 빅데이터 뉴스 타이틀", y=-0.1)
    plt.show()
