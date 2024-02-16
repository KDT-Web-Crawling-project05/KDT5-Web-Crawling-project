import matplotlib.pyplot as plt
import koreanize_matplotlib
from urllib.parse import quote
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

df = pd.read_csv('thesis_link.csv', index_col=[0])
recentDF = df[df['연도'] >= 2018]
sorted_recentDF = recentDF.sort_values(by=['연도'])

csv_dict = {'논문이름':[],
            '저자':[],
            '발행기관':[],
            '학술지명':[],
            '권호사항':[],
            '발행년도':[],
            '작성언어':[],
            '주제어':[],
            '초록':[]}
keywords_count = {}

# link = 'https://riss.kr' + recentDF.loc[0]['링크']
# print(link)

# driver = webdriver.Chrome()
# driver.get(link)
# driver.execute_script('goRelay()')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#
# detail = soup.select_one('div.searchDetail')
# info = detail.select_one('div.thesisInfo#thesisInfoDiv')
# additional = detail.select_one('div.innerCont#additionalInfoDiv')
# abstract = additional.select_one('div.content, div.addionalinfo')
# abs_text = abstract.select('div.text')[1]
# print(abs_text.text.strip())

cnt = 1
for idx in recentDF.index:
    link = 'https://riss.kr' + recentDF.loc[idx]['링크']

    driver = webdriver.Chrome()
    driver.get(link)
    driver.execute_script('goRelay()')
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    detail = soup.select_one('div.searchDetail')
    info = detail.select_one('div.thesisInfo#thesisInfoDiv')
    additional = detail.select_one('div.innerCont#additionalInfoDiv')

    csv_dict['논문이름'].append(detail.select_one('h3.title').text.strip().replace('\n', '').replace('\t', ''))
    print(csv_dict['논문이름'])

    li_list = info.select('ul > li')

    csv_dict['저자'].append(li_list[0].select_one('div').text.strip().replace('\n', '').replace('\t', ''))
    print(csv_dict['저자'])
    csv_dict['발행기관'].append(li_list[1].select_one('div').text.strip().replace('\n', '').replace('\t', ''))
    print(csv_dict['발행기관'])
    csv_dict['학술지명'].append(li_list[2].select_one('div').text.strip())
    print(csv_dict['학술지명'])
    csv_dict['권호사항'].append(li_list[3].select_one('div').text.strip().replace('\n', '').replace('\t', ''))
    print(csv_dict['권호사항'])
    csv_dict['발행년도'].append(li_list[4].select_one('div').text.strip())
    print(csv_dict['발행년도'])
    csv_dict['작성언어'].append(li_list[5].select_one('div').text.strip())
    print(csv_dict['작성언어'])

    if li_list[6].select_one('span').text == '주제어':
        csv_dict['주제어'].append(li_list[6].select_one('div').text.strip().replace('\n', '').replace('\t', ''))
        keywords = csv_dict['주제어'][-1].split(';')
        for word in keywords:
            word = word.strip()
            if word in keywords_count.keys():
                keywords_count[word] += 1
            else:
                keywords_count[word] = 1
    else:
        csv_dict['주제어'].append('')
    print(csv_dict['주제어'])
    print(cnt)
    cnt += 1

    try:
        abstract = additional.select_one('div.content, div.addionalinfo')
        abs_text = abstract.select('div.text')[1].text.strip()
        print(abs_text)
        print()
        csv_dict['초록'].append(abs_text)
    except Exception as e:
        print(e)
        csv_dict['초록'].append('')

    driver.close()

print('All data conformed')
print(csv_dict)
csv_df = pd.DataFrame(csv_dict)
csv_df.to_csv('thesis_info.csv', encoding='utf-8', index=False)
print('Exporting csv file is complete.')
print('keywords -- ')
print(keywords_count)

# 이놈들이 html파일을 바로 못가져오게 해놨다 얍삽한 녀석들
# print(soup)
# script = soup.select_one('head')
# driver.execute_script('goRelay()')
# print()
# print()
# print()
# soup2 = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup2.head)
# print()
# print()
# print()
# print(soup2.body)








