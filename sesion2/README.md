
__NOTA:__ 

Source:3e848bcca8f048587b6412a3eb5e43abe1a5cdbd


### REQUISITOS

```
git clone  --branch=v2 <este-repo>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### PRIMEROS PASOS

```
python3 workshop/ejemplo_sencillo_bs4.py
python3 workshop/ejemplo_sencillo_req.py
```
____

```
# set path
export PYTHONPATH="<your path>/deep-traslate/version1/deep_translator"

# added test
pytest test/test_deep_translator.py

```

cambios:

```
#deep_traslater.py
            # res = soup.find("div", {"class": "t0"})
            res = soup.find("div", {"class": "result-container"})
```

ejecutar el codigo:

```
python3 examples/trans.py
```

nuevos conceptos:

- pytest
- python import module

