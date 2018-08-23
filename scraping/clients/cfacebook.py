import time
import hashlib
from decouple import config
from selenium import webdriver


class FacebookClient:

    def __init__(self, names=None, np_posts=5, np_comments=10):
        self.names = names
        self.np_posts = np_posts
        self.np_comments = np_comments
        self.results = []

    def start(self):
        username = config('FACEBOOK_USER', default='localhost')
        password = config('FACEBOOK_PASSWORD', default='localhost')

        driver = webdriver.Firefox()
        driver.get('https://www.facebook.com/')
        driver.execute_script(f'document.getElementById("email").value = "{username}"')
        driver.execute_script(f'document.getElementById("pass").value = "{password}"')
        driver.find_element_by_id('loginbutton').click()
        time.sleep(5)

        for name in self.names:
            driver.get(f"https://www.facebook.com/pg/{name}/posts/?ref=page_internal")

            i = 1
            for _ in range(self.np_posts):
                m = i * 10000
                driver.execute_script(f"window.scrollTo(0, {m})")
                time.sleep(1)
                i += 1

            for _ in range(self.np_comments):
                links = driver.find_elements_by_class_name('UFIPagerLink')
                for link in links:
                    link.click()
                    time.sleep(.5)

            data = {
                'name': name,
                'comments': []
            }

            feeds = driver.find_elements_by_class_name('UFICommentContentBlock')
            for feed in feeds:
                try:
                    upost = feed.find_element_by_class_name('UFICommentActorAndBody')
                    username = upost.find_element_by_class_name('UFICommentActorName')
                    comment = upost.find_element_by_class_name('UFICommentBody')
                    dt = feed.find_element_by_class_name('UFISutroCommentTimestamp')

                    if username and comment:
                        username = username.text.strip()
                        comment = comment.text.strip()
                        tm = int(dt.get_attribute('data-utime'))

                        data['comments'].append({
                            'uuid': hashlib.sha256((username + '|' + comment).encode('ascii', 'ignore')).hexdigest(),
                            'username': username,
                            'data': time.strftime("%d/%m/%Y %H:%M", time.localtime(tm)),
                            'timestamp': tm,
                            'comment': comment
                        })
                except Exception as e:
                    print(f'ERROR: username or comment not found : {e}')
            self.results.append(data)
        driver.close()