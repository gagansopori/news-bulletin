import os, json, asyncio
from time import perf_counter, strftime, gmtime

from src.utility import filepath


class JsonParser:
    def __init__(self):
        self.source_urls = []

    def parse_json(self, df=None):
        if df is not None:
            self.url_parser_sync(df)
        else:
            with open(filepath, 'r') as source:
                begin = perf_counter()
                df = json.load(source)
                self.url_parser_sync(df)
                print(f'Time taken to parse Json: {perf_counter() - begin}')
        print(f'Source Size - {len(self.source_urls)}. \nURL List - {self.source_urls}')
        return self.source_urls

    def url_parser_sync(self, df):
        for item in df.values():
            if not isinstance(item, dict): # nested dictionary - the innermost level will not have dict as a value
                if item: # if that innermost level isn't empty
                    self.source_urls.append(item)
            else:
                self.url_parser_sync(item)
