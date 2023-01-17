



source:
f06c14ebdbcba5c07884ee5b16c27950990320b7


descripcion:
En este branch se adiciona un traductor.
- PONS


basica idea:

```
import requests
from requests.utils import quote
from bs4 import BeautifulSoup
_base_url = "https://en.pons.com/translate/"
_source = "spanish"
_target = "english"
payload = "ver"
url= "{}{}-{}/{}".format(_base_url, _source, _target, quote(payload))
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
res = soup.findAll("div", {"class":"target"})[0]
print(res.get_text(strip=True))
```

para ejecutar:

```
python3 deep_traslate.py
```