import requests,time
URL="https://realpython.com/atom.xml"
def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text
def main():
    start_time = time.time()
    get_article_from_server(URL)
    end_time = time.time()
    print(end_time-start_time)