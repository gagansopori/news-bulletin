# !/usr/bin/env python3

import json
from feedparser import parse


# TODO: Testing if title & description are present. Get more reliable news sources than bbc

class GetNewsBulletIn:
    def __init__(self):
        pass

    news_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'

    def parse_json(self, source_json):
        """
        This method will parse through the json file mentioned in the properties for news urls
        :param source_json:
        :return:
        """
        pass

    def fetch_news(self):
        """
        This method utilises feedparser.parse() to aggregate news from all the sources.
        :return:
        """
        try:
            return parse(self.news_url)
        except Exception:
            raise Exception
