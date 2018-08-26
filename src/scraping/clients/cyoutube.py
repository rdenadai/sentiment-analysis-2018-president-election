import time
import hashlib
from selenium import webdriver


class YouTubeClient:

    def __init__(self, np_posts=5, np_comments=10):
        self.np_posts = np_posts
        self.np_comments = np_comments
        self.results = {
            'network': 'youtube',
            'data': []
        }

    def start(self, name):
        driver = webdriver.Firefox()
        driver.get(name.uuid)

        i = 1
        for _ in range(self.np_posts):
            m = i * 2000
            driver.execute_script(f"window.scrollTo(0, {m})")
            time.sleep(1)
            i += 1

        data = {
            'name': name.name,
            'feed': []
        }

        feeds = []
        posts = driver.find_elements_by_tag_name('ytd-grid-video-renderer')
        for post in posts:
            link = post.find_element_by_tag_name('a')
            if link:
                feeds.append(link.get_attribute('href'))

        for feed in feeds:
            feed_data = {
                'feed_views_views': 0,
                'feed_views_likes': 0,
                'feed_views_dislikes': 0,
                'comments': []
            }

            driver.get(feed)
            time.sleep(1)

            try:
                views = driver.find_element_by_class_name('view-count').text
                feed_data['feed_views_views'] = int(views.split()[0].replace(',', ''))
            except Exception as e:
                print(f'ERROR: view count not found in tag : {e}')

            lds = driver.find_elements_by_tag_name('ytd-toggle-button-renderer')
            for ld in lds:
                try:
                    formatter = ld.find_element_by_tag_name('yt-formatted-string')
                    if formatter:
                        value = formatter.get_attribute('aria-label').strip()
                        if 'dislikes' in value:
                            feed_data['feed_views_dislikes'] = int(
                                value.replace(',', '').replace('dislikes', '').strip())
                        elif 'likes' in value:
                            feed_data['feed_views_likes'] = int(value.replace(',', '').replace('likes', '').strip())
                except Exception as e:
                    print(f'ERROR: Like / dislike not found in tag : {e}')

            pause = driver.find_element_by_class_name('ytp-play-button')
            if pause:
                pause.click()

            i = 1
            driver.execute_script(f"window.scrollTo(0, 500)")
            time.sleep(2)
            for _ in range(self.np_comments):
                m = i * 2000
                driver.execute_script(f"window.scrollTo(0, {m})")
                time.sleep(1)
                i += 1

            replies = driver.find_elements_by_tag_name('ytd-expander')
            for reply in replies:
                if 'View' in reply.text.strip():
                    try:
                        reply.find_element_by_id('more').click()
                    except Exception as e:
                        print(f'ERROR: element not found : {e}')
                    time.sleep(.5)

            user_posts = driver.find_elements_by_tag_name('ytd-comment-thread-renderer')
            for upost in user_posts:
                try:
                    username = upost.find_element_by_id('author-text')
                    comment = upost.find_element_by_id('content')
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
            data['feed'].append(feed_data)

        self.results['data'].append(data)
        driver.close()