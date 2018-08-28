import time
import hashlib
from selenium import webdriver
from utils import get_profile


class InstagramClient:

    def __init__(self, np_posts=5, np_comments=10):
        self.np_posts = np_posts
        self.np_comments = np_comments
        self.results = {
            'network': 'instagram',
            'data': []
        }

    def start(self, name):
        driver = webdriver.Firefox(firefox_profile=get_profile())
        driver.get(f"https://www.instagram.com/{name.uuid}/?hl=pt-br")

        for _ in range(self.np_posts):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

        feeds = []
        links = driver.find_elements_by_tag_name('a')
        for link in links:
            href = link.get_attribute('href')
            if f'taken-by={name.uuid}' in href:
                feeds.append(href)

        data = {
            'name': name.name,
            'feed': []
        }

        for feed in feeds:
            feed_data = {
                'feed_views_likes': 0,
                'comments': []
            }

            driver.get(feed)

            like = driver.find_element_by_xpath(
                "/html/body/span/section/main/div/div/article/div[2]/section[2]/div/span/span")
            feed_data['feed_views_likes'] = int(like.text.replace(',', ''))

            try:
                btn = driver.find_element_by_xpath("//button[contains(text(),'Load more comments')]")
                for _ in range(self.np_comments):
                    btn.click()
                    time.sleep(.5)
            except Exception as e:
                print(f'ERROR: No button to load more comments : {e}')

            try:
                user_posts = driver.find_elements_by_xpath('//ul/li/div/div/div')
                for upost in user_posts:
                    try:
                        username = upost.find_element_by_tag_name('a')
                        comment = upost.find_element_by_tag_name('span')
                        if username and comment:
                            username = username.text.strip()
                            comment = comment.text.strip()
                            feed_data['comments'].append({
                                'hash': hashlib.sha256((username + '|' + comment).encode('ascii', 'ignore')).hexdigest(),
                                'username': username,
                                'comment': comment
                            })
                    except Exception as e:
                        print(f'ERROR: username or comment not found : {e}')
            except Exception as e:
                print(f'ERROR: No Comments found : {e}')
            data['feed'].append(feed_data)

        self.results['data'].append(data)
        driver.close()