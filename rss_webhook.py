import requests
from bs4 import BeautifulSoup

rss_url = 'https://manga4life.com/rss/Kanojo-Okarishimasu.xml'
res = requests.get(rss_url)
soup = BeautifulSoup(res.text, features="xml")

title = soup.item.title.text
link = soup.item.link.text
date = soup.item.pubDate.text
print(f"{title}\n\n{link}\n\n{date}")

disc_url = 'https://discord.com/api/webhooks/1022953064577126451/q8HLKutcGFlL1HZ_eZDVftuBSi_eLvtJv67PP-TyHfmVKFKA9KPO5eIMvCQ12L2dceZA'
requests.post(disc_url, data={"content":title, "username": "Cap'n Hook"})