import requests
from bs4 import BeautifulSoup
url=("https://products.basf.com/global/en/ci/n-vinyl-2-pyrrolidone.html")
page_info=requests.get(url)
html_content=page_info.content
soup=BeautifulSoup(html_content,'html.parser')
print(soup.prettify)
print(soup.get_text())
paras=soup.find_all('p')
print(paras)
anchors=soup.find_all('a')
print(anchors)
link_text=""
for a in soup.find_all('a',href=True,text=True):
    link_text=a['href']
    print("link:"+link_text)


