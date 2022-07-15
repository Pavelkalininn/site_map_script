import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from threading import Thread


class SiteMap:

    def __init__(self, url: str):

        self.url: str = url
        self.site_urls: list = []
        self.url_map: dict = {}

    def __get_page_urls(self, url, map_level):
        # print('start')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        map_level[(title.text if title else '', url)] = {}

        print(map_level)
        urls = [href.get('href') for href in
                soup.find_all('a') + soup.find_all('link')]
        if urls:
            for current_url in urls:
                if (current_url
                        and current_url not in self.site_urls
                        and self.url + current_url not in self.site_urls
                ):
                    if self.url in current_url or current_url.startswith('/') and len(current_url) > 1:
                        if current_url.startswith('/') and len(current_url) > 1:
                            current_url = self.url + current_url
                        self.site_urls.append(current_url)
                        thread1 = Thread(target=self.__get_page_urls,
                                         args=(current_url,
                            map_level[(soup.find('title').text, url)]))
                        thread1.start()

                        # self.__get_page_urls(
                        #     current_url,
                        #     map_level[(soup.find('title').text, url)])

    def map_create(self):
        self.__get_page_urls(self.url, self.url_map)


if __name__ == '__main__':
    start = time.perf_counter()
    site = SiteMap('https://www.yandex.ru')
    site.map_create()
    finish = time.perf_counter()
    pprint(site.url_map)
    print('Time result', finish - start)

