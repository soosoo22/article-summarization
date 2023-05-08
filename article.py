import requests
from bs4 import BeautifulSoup

url = 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105'

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
#r = requests.get(url, headers=hdr)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
titles_html = soup.select('div.cluster_body > ul > li > div.cluster_text > a')
imgs_html = soup.find('div', 'cluster_thumb_inner').find('img')['src']
url_html = soup.find('div', 'cluster_text').find('a')['href']
#url_html = soup.select('div.cluster > div.cluster_group > div.cluster_body > ul > li > a')

#imgs_html = soup.select('div.cluster_thumb_inner > a > img')
#imgs_html = soup.select('#main_content > div > div._persist > div > div:nth-child(2) > div.cluster_body > ul > li:nth-child(1) > div.cluster_thumb > div > a > img')

print(url_html)

for i in range(len(titles_html)):
    print(i+1, imgs_html, titles_html[i].text)

