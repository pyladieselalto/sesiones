"""Main module."""

from bs4 import BeautifulSoup
import requests
from constants import BASE_URLS, LANGUAGES_TO_CODES

source = "es"
target = "en"
input_text = "Hola Gatitas y Gatitos"
def LanguageNotSupportedException(val, message="There is no support for the chosen language"):
    print(val, message)

def _validate_payload(payload):
    if not isinstance(payload, str):
        return False
    elif not payload:
        return False
    elif len(payload) > 5000:
        return False
    else:
        return True

def _map_language_to_code(language):
    if language in LANGUAGES_TO_CODES.values() or language == 'auto':
        return language
    elif language in LANGUAGES_TO_CODES.keys():
        return LANGUAGES_TO_CODES[language]
    else:
        raise LanguageNotSupportedException(language)

def _validate_languages(languages):
    for lang in languages:
        if lang != 'auto' and lang not in LANGUAGES_TO_CODES.keys():
            if lang != 'auto' and lang not in LANGUAGES_TO_CODES.values():
                raise LanguageNotSupportedException(lang)
    return True
def NotValidPayload(val,message='payload must be a valid text with maximum 5000 character, otherwise it cannot be translated'):
    print(f"{val} el error es {message}")

    
def translate(payload):
    valid = _validate_payload(payload)
    if not valid:
        raise NotValidPayload(payload)

    try:
        payload = payload.strip()
        params = {
                    "hl": _target,
                    "sl": _source,
                    "q": payload
        }

        res = requests.get(base_url, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')            
        # res = soup.find("div", {"class": "t0"})
        res = soup.find("div", {"class": "result-container"})
        return res.get_text(strip=True)

    except Exception as e:
        print(e.args)
        raise

base_url = BASE_URLS.get("GOOGLE_TRANSLATE")
if _validate_languages([source.lower(), target.lower()]):
    _source = _map_language_to_code(source.lower())
    _target = _map_language_to_code(target.lower())
    output_text=translate(payload=input_text)
    print(f"original texto: {input_text} | tranducido texto: {output_text}")  # output_text: fröhliche Codierung

