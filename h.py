import requests
from bs4 import BeautifulSoup as BS 

r = requests.get('https://stopgame.ru/review/new/stopchoice')
html = BS(r.content, 'html.parser')

for el in html.select('.lent-block'):
	title = el.select('.lent-title > a')
	coment = el.select('.lent-comments > a')
	print( title[0].text)
	print( coment[0].text)