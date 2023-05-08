from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
#from spacySum import summarized_text
from textrank import summ


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def chatting():

    #article.py
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100' #정치
    #url = 'https://sports.news.naver.com/index' #sports

    r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    #r = requests.get(url, headers=hdr)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('div.cluster_body > ul > li > div.cluster_text > a')
    imgs_html = soup.find('div', 'cluster_thumb_inner').find('img')['src']
    url_html = soup.find('div', 'cluster_text').find('a')['href']
    #imgs_html = soup.select('div.cluster_thumb_inner > a > img')
    #imgs_html = soup.select('#main_content > div > div._persist > div > div:nth-child(2) > div.cluster_body > ul > li:nth-child(1) > div.cluster_thumb > div > a > img')

    
    theme = []  #주제 배열
    urlArr = []   #url 배열
    for i in range(len(titles_html)):
        #print(i+1, imgs_html, titles_html[i].text)
        theme.append(titles_html[i].text)
        #urls.append(url_html[i])

    
    return render_template('index.html', source = imgs_html, theme = theme, url_html = url_html, apple = summ)

if __name__ == '__main__':
    app.debug = True
    app.run()





