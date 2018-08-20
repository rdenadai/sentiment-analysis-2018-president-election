import logging
import time
from selenium import webdriver


class TwitterClient:

    def __init__(self, names=None, np_posts=5, np_comments=10):
        self.names = names
        self.np_posts = np_posts
        self.np_comments = np_comments
        self.results = []

    def start(self):
        for name in self.names:
            driver = webdriver.Firefox()
            driver.get(f"https://twitter.com/{name}")

            for _ in range(self.np_posts):
                # for _ in range(scroll):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(1)

            data = {
                'name': name,
                'feed': []
            }

            feeds = []
            posts = driver.find_elements_by_xpath('//*[@id="stream-items-id"]/li/div')
            for post in posts:
                link = post.get_attribute('data-permalink-path')
                if link:
                    feeds.append('https://twitter.com%s' % link)

            for feed in feeds:
                feed_data = {
                    'feed_views_retweets': 0,
                    'feed_views_likes': 0,
                    'comments': []
                }

                driver.get(feed)

                retweets = driver.find_element_by_class_name('request-retweeted-popup').text
                feed_data['feed_views_retweets'] = int(retweets.replace('Retweets', '').replace(',', ''))
                likes = driver.find_element_by_class_name('request-favorited-popup').text
                feed_data['feed_views_likes'] = int(likes.replace('Likes', '').replace(',', ''))

                i = 0
                for _ in range(self.np_comments):
                    m = i * 2000
                    driver.execute_script(f"document.getElementById('permalink-overlay').scrollTo(0, {m})")
                    time.sleep(1)
                    i += 1

                replies = driver.find_elements_by_class_name('ThreadedConversation-moreRepliesLink')
                for reply in replies:
                    reply.click()
                    time.sleep(.5)

                replies_feed = driver.find_element_by_class_name('replies-to')
                if replies_feed:
                    user_posts = replies_feed.find_elements_by_class_name('content')
                    for upost in user_posts:
                        username = upost.find_element_by_class_name('username')
                        comment = upost.find_element_by_class_name('tweet-text')
                        if username and comment:
                            feed_data['comments'].append({
                                'username': (username.text).strip(),
                                'comment': (comment.text).strip()
                            })
                data['feed'].append(feed_data)

            self.results.append(data)
            driver.close()