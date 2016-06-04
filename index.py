import requests
import random
from lxml import html

url = "http://www.bash.org/?"
num = str(random.randrange(1, 2000))
print url + num
print "--------------------------"
headers = {'Accept-Encoding': 'identity'}
resp = requests.get('http://www.bash.org/?' + num, headers=headers)
tree = html.fromstring(resp.content)

quote = tree.xpath('//p[@class="qt"]/text()')
noquote = tree.xpath('//font[@class="bodytext"]/text()')

for quotebody in quote:
    item = quotebody.strip()
    restart = True
    while restart:
        if noquote != 1:
            print item
            restart = False
            break
        else:
            continue


#if resp.status_code != 200:
#    print Failed
#else:xpath('string(.)').extract()
#    print resp.text