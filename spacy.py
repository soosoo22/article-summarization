#pip3 install newspaper3k
#pip3 install spaCy
#python3 -m spacy download en_core_web_sm
     
#import spacySum
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
     

from newspaper import Article


url = 'https://sports.news.naver.com/news?oid=109&aid=0004843568'
#url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
article = Article(url)
article.download()
article.parse()
     
#기사 원문 출력
print(article.text)

def summarize(text, per):
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(text)
  tokens = [token.text for token in doc]
  word_frequencies={}
  for word in doc:
    if word.text.lower() not in list(STOP_WORDS):
      if word.text.lower() not in punctuation:
        if word.text not in word_frequencies.keys():
          word_frequencies[word.text] = 1
        else:
          word_frequencies[word.text] += 1
  max_frequency = max(word_frequencies.values())
  for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
  sentence_tokens = [sent for sent in doc.sents]
  sentence_scores = {}
  for sent in sentence_tokens:
    for word in sent:
      if word.text.lower() in word_frequencies.keys():
        if sent not in sentence_scores.keys():
          sentence_scores[sent] = word_frequencies[word.text.lower()]
        else:
          sentence_scores[sent]+=word_frequencies[word.text.lower()]
  select_length = int(len(sentence_tokens)*per)
  summary=nlargest(select_length, sentence_scores, key=sentence_scores.get)
  final_summary=[word.text for word in summary]
  summary=''.join(final_summary)
  return summary

     

# 5% 요약
summarized_text = summarize(article.text, 0.05)
print(summarized_text)