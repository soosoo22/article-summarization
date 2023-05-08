from gensim.summarization.summarizer import summarize
from newspaper import Article
import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100' #정치
#url = 'https://sports.news.naver.com/index' #sports

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
html = r.content
soup = BeautifulSoup(html, 'html.parser')
#titles_html = soup.select('div.cluster_body > ul > li > div.cluster_text > a')
#imgs_html = soup.find('div', 'cluster_thumb_inner').find('img')['src']
url_html = soup.find('div', 'cluster_text').find('a')['href']


news = Article(url_html, language='ko')
news.download()
news.parse()
#print(news.text)

# 문장 비율 설정
summ = summarize(news.text, ratio=0.1)
print(summ)
#summ = summarize(news.text, word_count=50)
#print(summ)