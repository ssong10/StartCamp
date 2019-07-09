import requests
from bs4 import BeautifulSoup

# url 가져오기
url = 'https://finance.naver.com/marketindex/'
# 요청보내기
response = requests.get(url).text
# html문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
# 하나 골라서 뽑아내기
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(f"{dollar}$")

# 1. url 설정
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 2. 요청 보내기
response = requests.get(url).text
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기
table = soup.select('body > div > table > tbody > tr')
# body > div > table > tbody > tr:nth-child(1) > td.sale
for tr in table:
    print(tr.select('td.sale'))