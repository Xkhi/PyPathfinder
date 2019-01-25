import requests
from bs4 import BeautifulSoup


index_url = 'http://pathfinder.d20srd.org/coreRulebook/spellIndex.html'
spell_root_url = 'http://pathfinder.d20srd.org/coreRulebook/'

index_raw = requests.get(index_url)
index_bs4 = BeautifulSoup(index_raw.text, 'html.parser')
spellList = index_bs4.find('div', {'id': 'spell-index-wrapper'})
spellList = spellList.findAll('a')

with open("SpellList.txt","w+") as spellFile:
    for spell in spellList:
        txt = spell_root_url+spell.attrs['href']
        buffer = BeautifulSoup(requests.get(txt).text, 'html.parser').find('div', {'class': 'body'})
        spellFile.write(buffer.text)
