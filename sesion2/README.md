
__NOTA:__ 

### REQUISITOS

TENEMOS 2 REPOS:

- https://github.com/mickhacking/PyladiesTranslator.git
- https://github.com/pyladieselalto/sesiones.git

```
git clone <lo-dos-repos>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Objetivos

Aprender un poco de Web.

cambios:

```
#deep_traslater.py
            # res = soup.find("div", {"class": "t0"})
            res = soup.find("div", {"class": "result-container"})
```


ejecutar el codigo:

```
python3 sesiones/sesion2/deep_traslator.py
```

nuevos conceptos:

- web
- webscraping

