import requests

def getSite(url):
    r = requests.get(url).text
    file = open('index.html', 'w')
    #print(r.text)
    file.write(r)
    #file.close()

getSite('http://ps.kz')


