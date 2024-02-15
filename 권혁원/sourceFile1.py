from urllib.parse import quote
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv

# keywords = ['인공지능', '생물정보학', '빅데이터', '데이터', '생물통계학']
# category = '의약학'

frontLink = ('https://riss.kr/search/Search.do?isDetailSearch=Y&searchGubun=true&viewYn=OP&queryText=znAll%2C인공지능%40op%2COR%40znAll%2C생물정보학%40op%2COR%40znAll%2C빅데이터%40op%2COR%40znAll%2C데이터%40op%2COR%40znAll%2C생물통계학&strQuery=&exQuery=l_sub_code%3A50◈&exQueryText=주제분류+%5B의약학%5D%40%40l_sub_code%3A50◈&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=2000&p_year2=2024&i'
            'StartCount=')
backLink = ('&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&db_type=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&'
            'pageScale=100'
            '&isTab=Y&regnm=&dorg_storage=&language=kor&language_code=&clickKeyword=&relationKeyword=&query=')
scount = 0

csv_dict = {'논문제목':[], '연도':[], '링크':[]}

while scount <= 900:
        driver = webdriver.Chrome()
        driver.get(frontLink + str(scount) + backLink)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        resultList = soup.select_one('div.srchResultListW')
        li_list = resultList.find_all('li')

        for li in li_list:
                try:
                        csv_dict['논문제목'].append(li.select_one('p.title > a').text)
                        csv_dict['연도'].append(li.select('p.etc > span')[2].text)
                        csv_dict['링크'].append(li.select_one('p.title > a').attrs['href'])
                except AttributeError:
                        continue

        driver.quit()

        scount += 100

print('link crawling completed')
DF = pd.DataFrame(csv_dict)
DF.to_csv('thesis_link.csv', encoding='utf-8')