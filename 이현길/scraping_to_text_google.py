from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
import time


def get_titles(start_num, end_num, search_word, title_list):
    while start_num < end_num:
        url = (
            f'https://scholar.google.co.kr/scholar?start={start_num}&q={search_word}')
        req = requests.get(url)
        time.sleep(2)
        print(req)
        if req.ok:
            soup = BeautifulSoup(req.text, 'html.parser')
            gs_res_ccl_mid = soup.find('div', {'id': 'gs_res_ccl_mid'})
            academic_title = gs_res_ccl_mid.find_all('h3', {'class': 'gs_rt'})
            for academic in academic_title:
                title_list.append(academic.text.strip())
        else:
            break
        start_num += 10
        print('title 개수:', len(title_list))
        # print(title_list)


if __name__ == '__main__':
    search_word = "빅데이터 활용"
    title_list = []

    get_titles(0, 990, search_word, title_list)

    with open('./DATA/title_list_google.txt', mode='w', encoding='utf-8') as f:
        f.write(str(title_list))
