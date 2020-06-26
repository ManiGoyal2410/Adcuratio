import requests  
import scrapy


class HackerNewsSpider(scrapy.Spider):
    name = 'blog_spider'
    start_urls = ['https://news.ycombinator.com']

    def parse(self, response):
        page_data = []
        item_list = response.xpath(
            '//table[@class="itemlist"]//tr[not(@class) or contains(@class, "athing")]')
        ele_for_next = item_list[-1]
        item_list = item_list[:-1]
        i = 0
        while i < len(item_list):
            data = {}
            data['title'] = item_list[i].xpath(
                './/a[@class="storylink"]/text()')[0].get()
            data['url'] = item_list[i].xpath(
                './/a[@class="storylink"]/@href')[0].get()
            data['id'] = int(item_list[i].xpath('./@id')[0].get())

            data['votes'] = int(
                item_list[i+1].xpath(
                    './/span[@class="score"]/text()')[0].get().split()[0])
            
            data['author'] = item_list[i+1].xpath(
                './/a[@class="hnuser"]/text()')[0].get()
            
            page_data.append(data)
            yield data
            
            i += 2