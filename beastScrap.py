import requests
from bs4 import BeautifulSoup
from utils import parse_url

rootUrl = 'http://pathfinder.d20srd.org/indices/bestiary.html'
baseUrl = 'http://pathfinder.d20srd.org'
monsterIndex = parse_url(rootUrl, tag='div', dict={'id': 'monster-index-wrapper'})

monsterList = monsterIndex.findAll('li')
with open('bestiary.html', 'w+') as destFile:
    destFile.write('<head><link rel="stylesheet" type="text/css" href="styles.css" media="screen" /></head>\n')
    destFile.write('<body>\n')
    for monster in monsterList:
        # monster.find('a').attrs['href'] = baseUrl + monster.find('a').attrs['href']
        destFile.write(str(monster))

    destFile.write('<p>Contents</p>\n')
    monsterUrlList = []
    for monster in monsterList:
        monsterUrl = baseUrl + monster.find('a').attrs['href'][2:]
        if monsterUrl not in monsterUrlList:
            monsterUrlList.append(monsterUrl)
            monsterData = parse_url(monsterUrl, tag='div', dict={'class': 'body'})
            try:
                monsterData.find('div', {'class': 'footer'}).decompose()
            except AttributeError:
                print(monster.text, 'has no footer')

            for p in monsterData:
                try:
                    destFile.write(str(p))
                except:
                    print('Error in', monster.text)
            destFile.write('\n\n')

    destFile.write('</body>')
