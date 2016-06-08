
import requests
import random
from lxml import html
import sys
import os

def search():
    url = "http://www.bash.org/?"
    num = str(random.randrange(1, 2000))
    print url + num
    print "--------------------------"
    headers = {'Accept-Encoding': 'identity'}
    resp = requests.get('http://www.bash.org/?' + num, headers=headers)
    tree = html.fromstring(resp.content)

    def quote():
        q_true = tree.xpath('//p[@class="qt"]/text()')
        for q_out in q_true:
            item = q_out.strip()
            return item

    def noquote():
        noq_true = tree.xpath('//font[@class="bodytext"]/text()')
        for noq_out in noq_true:
            print noq_out
        return
        
    return quote()

restart = True     
while restart:
    o_search = search()
    if o_search is None:
        continue
    else:
        o_search
        restart = False
        break