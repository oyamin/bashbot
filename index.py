import requests
import random
from lxml import html
import sys
import os

BASE_URL = "http://www.bash.org/"
MAX_NUM = 2000

def get_quote_lines(tree):
    q_true = tree.xpath('//p[@class="qt"]/text()')
    return [q_out.strip() for q_out in q_true]

def get_random_bash_url(max_num=MAX_NUM):
    num = str(random.randrange(1, max_num))
    return BASE_URL + '?' + num

def fetch_bash_quote(url):
    headers = {'Accept-Encoding': 'identity'}
    resp = requests.get(url, headers=headers)
    tree = html.fromstring(resp.content)
    return get_quote_lines(tree)

def main():
    restart = True     
    while restart:
        url = get_random_bash_url()
        o_search = fetch_bash_quote(url)
        if not o_search:
            continue
        else:
            print("Bash Quote from {}".format(url))
            print("----------------------------------------")
            print('\n'.join(o_search))
            restart = False
            break
    return
            
if __name__ == '__main__':
     main()
