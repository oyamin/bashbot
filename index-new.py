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
        q_true_out = []
        for q_out in q_true:
            item = q_out.strip()
            q_true_out.append(item)
            print q_true_out
            return q_true_out

    return quote()

search()

#    def noquote():
#        noq_true = tree.xpath('//font[@class="bodytext"]/text()')
#        for noq_out in noq_true:
#            print noq_out
#        return

repeat = True  
while repeat:
    for f_search in search():
    
        if f_search != None:
            print f_search
            repeat = False
            break
        
        else:
            print 'nothing'
            continue
