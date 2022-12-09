import feedparser
URL="https://dev.to/feed/"
feed = feedparser.parse(URL)
# Access Articles from Feed 
#print(feed['entries'])
# Get Number of Articles
#print(len(feedparser.parse(URL).entries))
# Get details of the entries from the feed 
 
for entry in feed.entries:
    print(f">{entry}")

#https://dev.to/mr_destructive/feedparser-python-package-for-reading-rss-feeds-5fnc