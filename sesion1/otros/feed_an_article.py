import request_an_article
import requests
import ssl
import time
import feedparser
URL= "https://realpython.com/atom.xml"
#print(request_an_article.get_article_from_server(URL))

#feedparser tries to access content served over HTTPS

if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context


def monitor(url):
    maxlen =  45
    while True:
        print("Convirtiendo el HTML")
        feed = feedparser.parse(url)
        
        for entry in feed.entries[:5]:
            print(f' entry es {entry}')
            if "python" in entry.title.lower():

                truncated_title = (

                    entry.title[:maxlen] + "..."

                    if len(entry.title) > maxlen

                    else entry.title

                )
                print(
                    "Match found:",
                    truncated_title,
                    len(request_an_article.get_article_from_server(entry.link)),
                )

        time.sleep(5)

monitor(URL)