import requests
from bs4 import BeautifulSoup
import time
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'port' : '8080'}
# html = requests.get("http://comic.kukudm.com/comiclist/2036/43239/3.htm",headers=headers).content
# soup = BeautifulSoup(html,"lxml")
# network= soup.find_all('script')[3].get_text().split('\"')[3].split("'")[0]
# picture = "http://n.1whour.com/"+ network
# pic = requests.get(picture,headers=headers).content
# f = open('1.jpg', 'wb')
# f.write(pic)
def geturl(urlx):
    try:
        text = requests.get(urlx,headers=headers).content
    except:
        time.sleep(5)
        text = geturl(urlx)
    return text
html = requests.get('http://comic.kukudm.com/comiclist/2036/',headers=headers).content
soup = BeautifulSoup(html,"lxml")
list = soup.find_all('a',href=re.compile(r"http://comic2.kukudm.com/comiclist/\d{4}/\d{5}/1.htm"))
y=1
for url in list:
    html_pic = geturl(url['href'])
    soup = BeautifulSoup(html_pic,"lxml")
    next = soup.find('a',href=re.compile(r"/comiclist/\d{4}/\d{5}/\d+\.htm"))
    pre_list = []
    pre_list.append(url['href'])
    while 1:
        print(y)
        network= soup.find_all('script')[3].get_text().split('\"')[3].split("'")[0]
        picture = "http://n.1whour.com/"+ network
        pic = geturl(picture)
        pic_name = "pic/"+str(y)+".jpg"
        f = open(pic_name, 'wb')
        y=y+1
        time.sleep(2)
        f.write(pic)
        str1 = "http://comic2.kukudm.com" + next['href']
        html_pic = geturl(str1)
        pre_list.append(str1)
        soup = BeautifulSoup(html_pic, "lxml")
        next_all = soup.find_all('a', href=re.compile(r"/comiclist/\d{4}/\d{5}/\d+\.htm"))
        if len(next_all)!=2:
            print(y)
            network = soup.find_all('script')[3].get_text().split('\"')[3].split("'")[0]
            picture = "http://n.1whour.com/" + network
            pic = geturl(picture)
            pic_name = "pic/" + str(y) + ".jpg"
            f = open(pic_name, 'wb')
            y = y + 1
            time.sleep(2)
            f.write(pic)
            break
        for nex in next_all:
            str2 = "http://comic2.kukudm.com" + nex['href']
            if str2 not in pre_list:
                next = nex
                break
        print(next)