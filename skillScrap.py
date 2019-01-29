import utils


core_url = 'http://pathfinder.d20srd.org/coreRulebook/skillDescriptions.html'
core_skill_url = 'http://pathfinder.d20srd.org/coreRulebook/'
skill_list = utils.parse_url(core_url)

skill_list = skill_list.findAll('tr')
url_list = []
for skill in skill_list:
    try:
        url_list.append(core_skill_url+skill.find('a').attrs['href'])
    except:
        print("Error in ", skill.text)

with open('skillScrap.html', 'w+') as dest_file:
    for url in url_list:
        try:
            temp = utils.parse_url(url, tag='div', dict={'class': 'body'})
            temp.find('div', {'class': 'footer'}).decompose()
            for i in temp:
                dest_file.write(str(i))
        except:
            print("Error in",url)

pass
