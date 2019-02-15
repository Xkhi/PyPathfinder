import utils


core_url = 'http://pathfinder.d20srd.org/coreRulebook/skillDescriptions.html'
core_skill_url = 'http://pathfinder.d20srd.org/coreRulebook/'
skill_list = utils.parse_url(core_url)

skill_list = skill_list.findAll('tr')

with open('skillScrap.html', 'w+') as dest_file:
    url_list = []
    dest_file.write('<head><link rel="stylesheet" type="text/css" href="styles.css" media="screen" /></head>\n')
    for skill in skill_list:
        try:
            url = core_skill_url + skill.find('a').attrs['href']
        except AttributeError:
            print(skill.text, 'has no link attr')
            url = 'Null'

        if url not in url_list and url is not 'Null':
            url_list.append(url)
            temp = utils.parse_url(url, tag='div', dict={'class': 'body'})
            try:
                temp.find('div', {'class': 'footer'}).decompose()
            except AttributeError:
                print('Skill', skill.text, 'has no footer')
            for i in temp:
                dest_file.write(str(i))
