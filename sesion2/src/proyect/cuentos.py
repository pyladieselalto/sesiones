from bs4 import BeautifulSoup
import requests
base_url = "https://www.muchoscuentos.com/cuentos-para-imaginar-1/pulgarcita/"
res = requests.get(base_url)
soup = BeautifulSoup(res.text, 'html.parser')            
# res = soup.find("div", {"class": "t0"})
res = soup.find("div", {"class": "cc-m-textwithimage-inline-rte"})
ans = res.find_all('p')
for x in ans:
    print(x.get_text().strip().replace('\n',''))