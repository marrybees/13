import requests
from bs4 import BeautifulSoup

url = 'https://biblusi.ge/search-result?q=%E1%83%A9%E1%83%A3%E1%83%9B%E1%83%90%E1%83%93%20%E1%83%A3%E1%83%9C%E1%83%93%E1%83%90%20%E1%83%98%E1%83%AF%E1%83%93%E1%83%94&page=1'
r = requests.get(url)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
body = soup.find("body")
title = soup.find('div', "დრო უნდა ჩერდებოდეს")
herf = soup.find('div', "/author/738")
style = soup.find('div', {'margin-left : -4px'})
