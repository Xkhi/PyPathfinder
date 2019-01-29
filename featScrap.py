import utils


rootUrl = 'http://pathfinder.d20srd.org/coreRulebook/feats.html'

featsList = utils.parse_url(rootUrl, tag='div', dict={'id': 'feats-text'})

with open('featList.html', 'w+') as dest_file:
    for elem in featsList:
        dest_file.write(str(elem))
