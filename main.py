from pprint import pprint

import requests
from bs4 import BeautifulSoup

#
# class Node:
#     def __init__(self, url):
#         self.url = url
#         self.title = None
#         self.children = []
#
#     def __str__(self):
#         return str(self.url) + ' ' + str([node.url for node in self.children])
#
#     def add_children(self, url):
#         self.children.append(Node(url))
#
#     def add_title(self, title):
#         self.title = title
#
#     def print_all(self, head):
#         for child in head.children:
#             print(child.url)
#             self.print_all(child)
#
#
# class SiteMap:
#
#     def __init__(self, url: str):
#         self.url: str = url
#         self.site_urls: list = []
#         self.url_map: dict = {}
#         self.head = Node(self.url)
#
#     def __get_page_urls(self, node):
#         print('start')
#         response = requests.get(node.url)
#         soup = BeautifulSoup(response.text, 'lxml')
#         node.add_title(soup.find('title').text)
#         urls = [href.get('href') for href in soup.find_all('a')]
#         #print(node)
#         if urls:
#             for current_url in urls:
#                 if self.url and current_url and self.url in current_url:
#                     if current_url not in self.site_urls:
#                         self.site_urls.append(current_url)
#                         self.__get_page_urls(Node(current_url))
#                         # for elem in node.children:
#                         #
#                         #     print(elem)
#                             # for other_elem in elem:
#                             #
#                             #     print(other_elem)
#                         print(current_url)
#                         yield current_url
#
#
#     def map_create(self):
#
#         for x in self.__get_page_urls(self.head):
#             print(x)
#         # for page_urls in self.__get_page_urls(self.url, node):
#


class SiteMap:

    def __init__(self, url: str):

        self.url: str = url
        self.site_urls: list = []
        self.url_map: dict = {}

    def __get_page_urls(self, url, map_level):
        print('start')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        map_level[(title.text if title else '', url)] = {}

        print(map_level)
        urls = [href.get('href') for href in soup.find_all('a') + soup.find_all('link')]
        if urls:
            for current_url in urls:
                if current_url not in self.site_urls and url.split(current_url)[0] not in self.site_urls:
                    print('!!!', self.site_urls)
                    print('+++', url.split(current_url)[0])
                    if self.url in current_url:
                        self.site_urls.append(current_url)
                        self.__get_page_urls(current_url, map_level[(soup.find('title').text, url)])
                    elif current_url.startswith('/') and len(current_url) > 1:
                        self.site_urls.append(url.strip('/') + current_url)
                        print('startwith')
                        self.__get_page_urls(url.strip('/') + current_url, map_level[
                            (soup.find('title').text, url)])
    def map_create(self):
        self.__get_page_urls(self.url, self.url_map)


if __name__ == '__main__':
    site = SiteMap('https://www.hostcms.ru')
    site.map_create()
    pprint(site.url_map)

