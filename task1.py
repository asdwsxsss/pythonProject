import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'

heroes = requests.get(url)
my_heroes = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}
for hero in heroes.json():
    if hero['name'] in my_heroes:
        intelligence[hero['name']] = hero['powerstats']['intelligence']
intelligence_heroes = dict([max(intelligence.items(), key=lambda k_v: k_v[1])])
print(intelligence_heroes)