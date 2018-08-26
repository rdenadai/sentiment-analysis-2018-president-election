import time
import hashlib
from selenium import webdriver


class TwitterTagsClient:

    def __init__(self, np_posts=5):
        self.np_posts = np_posts
        self.results = []
        self.results = {
            'data': []
        }

    def start(self, hashtag):

        driver = webdriver.Firefox()
        driver.get(f"https://twitter.com/hashtag/{hashtag}")

        for _ in range(self.np_posts):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

        data = {
            'hashtag': hashtag,
            'comments': []
        }

        tweets = driver.find_elements_by_class_name('tweet')
        for tweet in tweets:
            try:
                username = tweet.find_element_by_class_name('username')
                comment = tweet.find_element_by_class_name('tweet-text')
                dt = tweet.find_element_by_class_name('_timestamp')

                if username and comment:
                    username = username.text.strip()
                    comment = comment.text.strip()
                    tm = int(dt.get_attribute('data-time'))

                    data['comments'].append({
                        'hash': hashlib.sha256((username + '|' + comment).encode('ascii', 'ignore')).hexdigest(),
                        'username': username,
                        'data': time.strftime("%d/%m/%Y %H:%M", time.localtime(tm)),
                        'timestamp': tm,
                        'comment': comment
                    })
            except Exception as e:
                print(f'ERROR: username or comment not found : {e}')
        self.results['data'].append(data)
        driver.close()
