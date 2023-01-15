import requests
from bs4 import BeautifulSoup
_base_url= "https://translate.google.com/m"
translate_endpoint = "translate"
api_key = "some-key"
_source = "en"
_target = "es"
text = "Usage of excessive, extreme or inappropriate language is prohibited."
params = {
"sl": _source,
"tl": _target,
"q": text}
response = requests.get(_base_url, params=params )
soup = BeautifulSoup(response.text, "html.parser")
element = soup.find("div", {"class":"result-container"})
print(element.text)