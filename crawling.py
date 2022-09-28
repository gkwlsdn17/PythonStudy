from bs4 import BeautifulSoup
import requests

html = ''
headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
res = requests.get("http://www.melon.com/chart/index.htm", headers=headers)
content = BeautifulSoup(res.content, 'html.parser')
tag_list = []
for tr_tag in content.find_all('tr'):
    tag = tr_tag.find(class_='wrap_song_info')
    if(tag):
        tag_sub_list = tag.find_all(href=lambda value: (value and 'playSong' in value))
        tag_list.extend(tag_sub_list)

        for idx, tag in enumerate(tag_list, 1):
            print(idx, tag.text)

# print(content)
