import requests

#probelma
"""
def get_article_from_server(url):
    print("realizando peticion")
    response = requests.get(url)
    return None
get_article_from_server("https://realpython.com/sorting-algorithms-python/")
get_article_from_server("https://realpython.com/sorting-algorithms-python/")
"""

cache = dict()

def get_article_from_server(url):
    print("Pedir recurso...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")
