from bs4 import BeautifulSoup
import requests
import pandas as pd


headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

# page = "https://www.transfermarkt.de/premier-league/transfers/wettbewerb/GB1"
page = "https://www.transfermarkt.de/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=2017&s_w=&leihe=0&intern=0"
# page = "https://www.whoscored.com/Players/346300/Show/Jadon-Sancho"

# page = "https://www.whoscored.com/Teams/44/Show/Germany-Borussia-Dortmund"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

print(pageSoup.prettify())