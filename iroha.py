import requests
from bs4 import BeautifulSoup
import os
url = 'https://www.joa-technology.com/'
response = requests.get(url)
# ページのHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')
# 例：見出し（h1）を取得
h1 = soup.find_all('h2', class_='elementor-heading-title elementor-size-default')
for h in h1:
    print(h.get_text())


os.makedirs('haruharu', exist_ok=True)

for img in soup.find_all('img'):
    img_url=img.get('src')
    img_name=img.get("alt")
    print(img_url)
    img_data = requests.get(img_url).content
    with open(os.path.join("./",img_name+".jpg"),'wb')as f:
        f.write(img_data)