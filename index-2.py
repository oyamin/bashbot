import requests
import random
from lxml import html
import sys
import os



def search():
    url = "http://www.bash.org/?"
    num = str(random.randrange(1, 2000))
    headers = {'Accept-Encoding': 'identity'}
    resp = requests.get('http://www.bash.org/?' + num, headers=headers)
    tree = html.fromstring(resp.content)

    def quote():
        q_true = tree.xpath('//p[@class="qt"]/text()')
        items = []
        for q_out in q_true:
            item = q_out.strip()
            items.append(item)
		return items
        
    return quote()

restart = True     
while restart:
    o_search = search()
    if o_search :
        continue
    else:
        print "Bash Quote"
        print o_search
        restart = False
        break