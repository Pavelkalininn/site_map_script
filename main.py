import json
import logging
import time

import requests
from bs4 import BeautifulSoup
from threading import Thread

HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0)'
        ' Gecko/20100101 Firefox/45.0'
}


class SiteMap:

    def __init__(self, main_url: str):

        self.main_url: str = main_url
        self.site_urls: list = [main_url, main_url + '/']
        self.url_map: dict = {}
        self.prefix = self.main_url.split('//')[0]

    def __get_response(self, response_url):
        try:
            return requests.get(response_url, headers=HEADERS)
        except requests.exceptions.ConnectionError as error:
            logging.error(error, exc_info=True)
            return ''

    def __get_page_urls(self, url, map_level):
        response = self.__get_response(url)
        if not response:
            return
        soup = BeautifulSoup(response.text, 'lxml')
        map_level[url] = {}
        urls = [href.get('href') for href in
                soup.find_all('a') + soup.find_all('link')]
        threads = []
        if urls:
            for current_url in urls:
                if current_url and (
                        (self.main_url in current_url)
                        or (current_url.startswith('/')
                            and len(current_url) > 1)
                ):
                    if (current_url.startswith('/')
                            and len(current_url) > 1
                            and not current_url.startswith('//')):
                        current_url = self.main_url + current_url
                    if current_url.startswith('//'):
                        current_url = self.prefix + current_url
                    if (current_url not in self.site_urls
                            and self.main_url in current_url
                    ):
                        self.site_urls.append(current_url)
                        threads.append(
                            Thread(
                                target=self.__get_page_urls,
                                args=(current_url,
                                      map_level[url])))

        for thread in threads:
            thread.start()
            thread.join()

    def map_create(self):
        self.__get_page_urls(self.main_url, self.url_map)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename='map1.log',
        format=f'%(asctime)s, %(levelname)s, %(message)s, %(name)s')

    input_urls = [
        'http://google.com/',
        'http://crawler-test.com/',
        'https://vk.com',
        'https://yandex.ru',
        'https://stackoverflow.com',
    ]
    for url in input_urls:
        logging.info(f'Start {url} mapping')
        filename = url.split('//')[-1].split('www.')[-1].split('.')[0] + '.txt'
        start = time.perf_counter()
        site = SiteMap(url.strip('/'))
        site.map_create()
        finish = time.perf_counter()
        timing = str(finish - start)
        message = (
                url
                + ' time: '
                + timing
                + ' url count: '
                + str(len(site.site_urls) - 1)
                + ' filename: '
                + filename
        )
        logging.info(message)
        with open(filename, 'w') as outfile:
            json.dump(site.url_map, outfile)
        logging.info(f'File {filename} successfully created')
