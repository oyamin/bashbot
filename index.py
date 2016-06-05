import requests
import random
from lxml import html
import sys
import os

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
        print item
    return

def noquote():
    noq_true = tree.xpath('//font[@class="bodytext"]/text()')
    for noq_out in noq_true:
        print noq_out
    return
       
restart = True     
while restart:
    restart = False
    f_quote = quote()
    f_noquote = noquote()
    if f_noquote is None:
        f_quote
    elif f_noquote:
        f_noquote
        restart = True
        
       


    



            
            



#if resp.status_code != 200:
#    print Failed
#else:xpath('string(.)').extract()
#    print resp.tex