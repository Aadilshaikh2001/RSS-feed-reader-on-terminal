# Rss-feed-reader 
# website Link: https://feedparser.readthedocs.io/en/latest/examples/rss20.xml
# Help from Link: https://feedparser.readthedocs.io/en/latest/common-rss-elements.html

import feedparser

data = feedparser.parse(input('Enter you URl:'))

for entry in data:
    Title = data.feed.title
    des = data.feed.description
    link = data.feed.link
    print(f'\nTitle: {Title}\n\nDescription: {des}\n\nLink: {link}\n\n--------------------------------------------------------------------------------\n\n')