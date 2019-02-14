import requests
from bs4 import BeautifulSoup
from utils import parse_url

rootUrl = 'http://pathfinder.d20srd.org/indices/bestiary.html'
baseUrl = 'http://pathfinder.d20srd.org'
monsterIndex = parse_url(rootUrl, tag='div', dict={'id': 'monster-index-wrapper'})

monsterList = monsterIndex.findAll('li')
with open('bestiary.html', 'w+') as destFile:
    destFile.write('Alphabetical Index')
    for monster in monsterList:
        # monster.find('a').attrs['href'] = baseUrl + monster.find('a').attrs['href']
        destFile.write(str(monster))

    destFile.write('Contents')
    for monster in monsterList:
        monsterUrl = baseUrl + monster.find('a').attrs['href'][2:]
        monsterData = parse_url(monsterUrl, tag='div', dict={'class': 'body'})
        for p in monsterData:
            destFile.write(str(p))
        break
