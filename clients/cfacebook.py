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
            driver.get(f"https://www.facebook.com/pg/{name}/posts/?ref=page_internal")

            i = 1
            for _ in range(self.np_posts):
                m = i * 10000
                driver.execute_script(f"window.scrollTo(0, {m})")
                time.sleep(1)
                i += 1

            links = driver.find_elements_by_class_name('UFIPagerLink')
            for link in links:
                link.click()
                time.sleep(.5)

            data = {
                'name': name,
                'feed_views_likes': 0,
                'comments': []
            }

            self.results.append(data)
            # driver.close()