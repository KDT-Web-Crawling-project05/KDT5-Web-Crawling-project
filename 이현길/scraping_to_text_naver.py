from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import time
import re


def get_titles(start_num, end_num, search_word, title_list, year_list):
    count = 0
    pre_len = 0
    while start_num <= end_num:
        url = (
            f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}&start={start_num}')
        # start_num ~ end_num까지 크롤링
        req = requests.get(url)
        time.sleep(1)
        regex_this_year = re.compile('^.*전')
        regex_year = re.compile('\..*')
        if req.ok:  # 정상적인 request 확인
            soup = BeautifulSoup(req.text, 'html.parser')
            news_area = soup.find_all('div', {'class':'news_area'})
            for news in news_area:
                news_title = news.find('a', {'class':'news_tit'})
                if news_title['title'] not in title_list:
                    title_list.append(news_title['title'])
                    news_year = news.find_all('span', {'class':'info'})
                    for year in news_year:
                        if "spnew ico_paper" in str(object=year):
                            continue
                        if year.text.endswith('전'):
                            year_list.append(regex_this_year.sub('2024', year.text))
                        else:
                            year_list.append(regex_year.sub('', year.text))
        else:
            break

        start_num += 10
        print('title 개수:', len(title_list))
        print('year 개수:', len(year_list))

        if pre_len == len(title_list):
            count += 1
        else:
            count = 0
        pre_len = len(title_list)

        if count > 10:
            break


if __name__ == '__main__':
    search_word = '"바이오 빅데이터"'
    title_list = []
    year_list = []

    get_titles(1, 10000, search_word, title_list, year_list)

    with open('./DATA/title_list_naver.txt', mode='w', encoding='utf-8') as ftitle:
        ftitle.write(str(title_list))
    with open('./DATA/year_list_naver.txt', mode='w', encoding='utf-8') as fyear:
        fyear.write(str(year_list))

    print(title_list)
    print('-' * 100)
    print(year_list)
