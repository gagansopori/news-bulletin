import os

resource_path = os.path.realpath('src/resources')
print(f'resource_path - {resource_path}')
filepath = os.path.join(resource_path, 'source_urls.json')
print(f'filepath - {filepath}')



# Option - 1
"""
{
  "news": {
    "bbc": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "cnn": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "fox": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "cnbc": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "yahoo": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "npr": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "abc": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "cbs": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "politico": {"world": "url", "sports": "url", "finance": "url","technology": "url", "entertainment": "url"},
    "Indian Express": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
    "The Hindu": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
  }
}
"""

# Option - 2
"""
{
  "news": {
    "us": {
      "cnn": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
      "fox": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"}
    },
    "in": {
      "NDTV": {"top": "https://feeds.feedburner.com/ndtvnews-top-stories", "world": "https://feeds.feedburner.com/ndtvnews-world-news", "sports": "https://feeds.feedburner.com/ndtvsports-latest", "finance": "https://feeds.feedburner.com/ndtvprofit-latest", "technology": "https://feeds.feedburner.com/gadgets360-latest", "entertainment": "https://feeds.feedburner.com/ndtvmovies-latest"},
      "India Today": {"top": "https://www.indiatoday.in/rss/1206584", "world": "https://www.indiatoday.in/rss/1206577", "sports": "https://www.indiatoday.in/rss/1206550", "finance": "https://www.indiatoday.in/rss/1206513", "technology": "url", "entertainment": "url"},
      "Indian Express": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
      "The Hindu": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
      "News 18": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
      "Firstpost": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
      "Zee News": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"},
      "Hindustan Times": {"world": "url", "sports": "url", "finance": "url", "technology": "url", "entertainment": "url"}
    }
  }
}
"""

# Option - 3
"""
{
  "news": {
    "world": {"bbc": "url", "cnn": "url", "fox": "url","cnbc": "url", "yahoo": "url"},
    "sports": {"cnn": "url", "fox": "url", "espn": "url","yahoo": "url", "npr": "url"},
    "finance": {"cnbc": "url", "fox": "url", "npr": "url","msn": "url", "yahoo": "url"},
    "technology": {"yahoo": "url", "msn": "url", "npr": "url","abc": "url", "cbs": "url"},
    "entertainment": {"ftv": "url", "hooters": "url", "avn": "url","xbiz": "url", "et": "url"},
    "politics": {"npr": "url", "politico": "url", "cnn": "url","fox": "url", "cbs": "url"},
    "weather": {"npr": "url", "weatherchannel": "url", "some-other-shit": "url","noshit": "url", "noshitmf": "url"}
  }
}
"""

# le_news = {
#   "news": {
#     "entertainment": {"avn": "url", "et": "url", "ftv": "url", "hooters": "url", "xbiz": "url"},
#     "finance": {"cnbc": "url", "fox": "url", "msn": "url", "npr": "url", "yahoo": "url"},
#     "politics": {"cbs": "url", "cnn": "url", "fox": "url", "npr": "url", "politico": "url"},
#     "sports": {"cnn": "url", "espn": "url", "fox": "url", "npr": "url", "yahoo": "url"},
#     "technology": {"abc": "url", "cbs": "url", "msn": "url", "npr": "url", "yahoo": "url"},
#     "weather": {"noshit": "url", "noshitmf": "url", "npr": "url", "sos": "url", "weatherchannel": "url"},
#     "world": {
#       "bbc": "http://feeds.bbci.co.uk/news/world/rss.xml",
#       "buzzfeed": "https://www.buzzfeed.com/world.xml",
#       "cnbc": "https://www.cnbc.com/id/100727362/device/rss/rss.html",
#       "cnn": "http://rss.cnn.com/rss/edition_world.rss",
#       "fox": "https://moxie.foxnews.com/google-publisher/world.xml",
#       "npr": "https://feeds.npr.org/1004/rss.xml",
#       "nytimes": "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
#       "un": "https://news.un.org/feed/subscribe/en/news/all/rss.xml",
#       "washingtonpost": "https://feeds.washingtonpost.com/rss/world", # This is not rss (Very Heavy)
#       "ndtv": "https://feeds.feedburner.com/ndtvnews-world-news",
#       "indiatoday": "https://www.indiatoday.in/rss/1206577",
#       "indianexpress": "https://indianexpress.com/section/world/feed/",
#       "thehindu": "https://www.thehindu.com/news/national/?service=rss",
#       "wsj": "https://feeds.a.dj.com/rss/RSSWorldNews.xml"
#     }
#   }
# }

"""
{
  "news": {
    "entertainment": {
      "adult": {"xbiz": "https://www.xbiz.com/rss/news/all.xml", "avn": "https://avn.com/feed/articles/video.rss",
        "us": {
          "xbiz": {
            "business": "https://www.xbiz.com/rss/features/business.xml",
            "europe": "https://www.xbiz.com/rss/news/europe.xml",
            "events": "https://www.xbiz.com/rss/events/all.xml",
            "movies-stars": "https://www.xbiz.com/rss/news/movies-stars.xml",
            "opinion": "https://www.xbiz.com/rss/features/opinion.xml",
            "photos": "https://www.xbiz.com/rss/photos/all.xml",
            "profile": "https://www.xbiz.com/rss/features/profile.xml",
            "reviews": "https://www.xbiz.com/rss/movies/reviews.xml",
            "top-stories": "https://www.xbiz.com/rss/news/all.xml",
            "web-tech": "https://www.xbiz.com/rss/news/web-tech.xml"
          },
          "avn": {
            "news": "https://avn.com/feed/articles/video.rss"
          }
        }
      },
      "avn": "url",
      "et": "url",
      "ftv": "url",
      "hooters": "url",
      "xbiz": "url"
    },
    "finance": {
      "cnbc": "url",
      "fox": "url",
      "msn": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "politics": {
      "cbs": "url",
      "cnn": "url",
      "fox": "url",
      "npr": "url",
      "politico": "url"
    },
    "sports": {
      "cnn": "url",
      "espn": "url",
      "fox": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "technology": {
      "abc": "url",
      "cbs": "url",
      "msn": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "weather": {
      "noshit": "url",
      "noshitmf": "url",
      "npr": "url",
      "some-other-shit": "url",
      "weatherchannel": "url"
    },
    "world": {
      "bbc": "http://feeds.bbci.co.uk/news/world/rss.xml",
      "cnbc": "https://www.cnbc.com/id/100727362/device/rss/rss.html",
      "cnn": "http://rss.cnn.com/rss/edition_world.rss",
      "fox": "https://moxie.foxnews.com/google-publisher/world.xml",
      "indiatoday": "https://www.indiatoday.in/rss/1206577",
      "ndtv": "https://feeds.feedburner.com/ndtvnews-world-news",
      "npr": "https://feeds.npr.org/1004/rss.xml",
      "nytimes": "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
      "nytimeslite": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
      "thehindu": "https://www.thehindu.com/news/national/?service=rss",
      "un": "https://news.un.org/feed/subscribe/en/news/all/rss.xml"
    }
  }
}"""



# Another Prospect

"""
{
  "news": {
    "top-stories": {

    },
    "entertainment": {
      "adult": {
        "xbiz": "https://www.xbiz.com/rss/news/all.xml",
        "avn": "https://avn.com/feed/articles/video.rss"
      },
      "events": {
      },
      "fashion": {
        "et": "https://www.etonline.com/style/fashion/rss",
        "vogue": "https://www.vogue.com/feed/fashion/rss",
        "elle": "https://www.elle.com/rss/fashion.xml",
        "gq": "https://www.gq.com/feed/style/rss",
        "harper-bazaar": "https://www.harpersbazaar.com/rss/fashion/"
      },
      "lifestyle": {
        "et": "https://www.etonline.com/style/lifestyle/rss",
        "vogue": "https://www.vogue.com/feed/living/rss",
        "elle": "https://www.elle.com/rss/life-love.xml"
      },
      "shopping": {
        "gq": "https://www.gq.com/feed/gq-recommends/rss"
      },
      "top-stories": {
        "et": "https://www.etonline.com/news/rss",
        "ftv": "url",
        "gq": "https://www.gq.com/feed/rss",
        "elle": "https://www.elle.com/rss/all.xml "
      },
      "culture": {
        "vogue": "https://www.vogue.com/feed/culture/rss",
        "elle": "https://www.elle.com/rss/culture.xml",
        "gq": "https://www.gq.com/feed/culture/rss",
        "harper-bazaar": "https://www.harpersbazaar.com/rss/culture/"
      },
      "tv-films": {
        "et": "https://www.etonline.com/movies/rss",
        "harper-bazaar": "https://www.harpersbazaar.com/rss/celebrity/"
      },
      "health-beauty": {
        "vogue": "https://www.vogue.com/feed/beauty/rss",
        "harper-bazaar": "https://www.harpersbazaar.com/rss/beauty/"
      }
    },
    "finance": {
      "cnbc": "url",
      "fox": "url",
      "msn": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "politics": {
      "cbs": "url",
      "cnn": "url",
      "fox": "url",
      "npr": "url",
      "politico": "url"
    },
    "sports": {
      "cnn": "url",
      "espn": "url",
      "fox": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "technology": {
      "abc": "url",
      "cbs": "url",
      "msn": "url",
      "npr": "url",
      "yahoo": "url"
    },
    "weather": {
      "noshit": "url",
      "noshitmf": "url",
      "npr": "url",
      "some-other-shit": "url",
      "weatherchannel": "url"
    },
    "world": {
      "bbc": "http://feeds.bbci.co.uk/news/world/rss.xml",
      "cnbc": "https://www.cnbc.com/id/100727362/device/rss/rss.html",
      "cnn": "http://rss.cnn.com/rss/edition_world.rss",
      "fox": "https://moxie.foxnews.com/google-publisher/world.xml",
      "indiatoday": "https://www.indiatoday.in/rss/1206577",
      "ndtv": "https://feeds.feedburner.com/ndtvnews-world-news",
      "npr": "https://feeds.npr.org/1004/rss.xml",
      "nytimes": "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
      "nytimeslite": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
      "thehindu": "https://www.thehindu.com/news/national/?service=rss",
      "un": "https://news.un.org/feed/subscribe/en/news/all/rss.xml"
    }
  }
}
"""


# This seems to be the most promising DS as of 2/14/2023
"""
{
  "top-stories": {},
  "entertainment": {
    "adult": {
      "avn": "https://avn.com/feed/articles/video.rss",
      "xbiz": "https://www.xbiz.com/rss/news/all.xml"
    },
    "culture": {
      "elle": "https://www.elle.com/rss/culture.xml",
      "gq": "https://www.gq.com/feed/culture/rss",
      "harper-bazaar": "https://www.harpersbazaar.com/rss/culture/",
      "vogue": "https://www.vogue.com/feed/culture/rss"
    },
    "fashion": {
      "elle": "https://www.elle.com/rss/fashion.xml",
      "et": "https://www.etonline.com/style/fashion/rss",
      "gq": "https://www.gq.com/feed/style/rss",
      "harper-bazaar": "https://www.harpersbazaar.com/rss/fashion/",
      "vogue": "https://www.vogue.com/feed/fashion/rss"
    },
    "health-beauty": {
      "harper-bazaar": "https://www.harpersbazaar.com/rss/beauty/",
      "vogue": "https://www.vogue.com/feed/beauty/rss"
    },
    "lifestyle": {
      "elle": "https://www.elle.com/rss/life-love.xml",
      "et": "https://www.etonline.com/style/lifestyle/rss",
      "vogue": "https://www.vogue.com/feed/living/rss"
    },
    "shopping": {
      "gq": "https://www.gq.com/feed/gq-recommends/rss"
    },
    "top-stories": {
      "elle": "https://www.elle.com/rss/all.xml ",
      "et": "https://www.etonline.com/news/rss",
      "ftv": "url",
      "gq": "https://www.gq.com/feed/rss"
    },
    "tv-films": {
      "et": "https://www.etonline.com/movies/rss",
      "harper-bazaar": "https://www.harpersbazaar.com/rss/celebrity/"
    },
    "events": {}
  },
  "finance": {},
  "politics": {},
  "sports": {},
  "technology": {},
  "weather": {},
  "world": {
    "africa": {},
    "asia": {
      "indiatoday": "https://www.indiatoday.in/rss/1206577", 
      "ndtv": "https://feeds.feedburner.com/ndtvnews-world-news",
      "thehindu": "https://www.thehindu.com/news/national/?service=rss"
    },
    "europe": {
      "bbc": "http://feeds.bbci.co.uk/news/world/rss.xml"
    },
    "north-america": {
      "cnbc": "https://www.cnbc.com/id/100727362/device/rss/rss.html", 
      "cnn": "http://rss.cnn.com/rss/edition_world.rss", 
      "fox": "https://moxie.foxnews.com/google-publisher/world.xml", 
      "npr": "https://feeds.npr.org/1004/rss.xml", 
      "nytimes": "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
      "nytimeslite": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    },
    "oceania": {},
    "south-america": {}
  }
}
"""