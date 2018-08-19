import logging
import time
from selenium import webdriver


class FacebookClient:

    def __init__(self, names=None, np_posts=5, np_comments=10):
        self.names = names
        self.np_posts = np_posts
        self.np_comments = np_comments
        self.results = []

    def start(self):
        for name in self.names:
            driver = webdriver.Firefox()
            driver.get(f"https://www.facebook.com/{name}/")

            for _ in range(self.np_posts):
                # for _ in range(scroll):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)

            data = {
                'name': name,
                'feed_views_likes': 0,
                'comments': []
            }

            self.results.append(data)
            driver.close()