# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class SDoubanSpider(scrapy.Spider):
    name = 's_douban'
    #allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/']

    # def start_requests(self):
    #     url = 'https://www.douban.com/'
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    #
    #     }
    #     yield scrapy.Request(url=url,headers=headers)

    def parse(self, response):
        cookies=response.request.headers.getlist('cookie')
        # print(cookies)
        print(response.status)
        try:
            username=response.xpath('//li[@class="nav-user-account"]/a/span[1]/text()').get()
            print(username)
        except Exception as e:
            print(e)
        book_url='https://book.douban.com'
        yield scrapy.Request(book_url,callback=self.book_base_parse)

    def book_base_parse(self,response):
        more_new_books=response.request.url+response.xpath('//div[@class="hd"]/h2/span[2]/a/@href').get()
        yield scrapy.Request(more_new_books,callback=self.more_new_books_parse)
        print(more_new_books)

    def more_new_books_parse(self,response):
        item=DoubanItem()
        booknames=response.xpath('//div[@id="content"]//ul/li/preceding-sibling::*/div/h2/a/text()').extract()
        book_urls=response.xpath('//div[@id="content"]//ul/li/preceding-sibling::*/div/h2/a/@href').extract()
        authors=response.xpath('////div[@id="content"]//ul/li/preceding-sibling::*/div/p[2]/text()').extract()
        book_abstracts=response.xpath('//div[@id="content"]//ul/li/preceding-sibling::*/div/p[3]/text()').extract()

        # print(len(book_abstracts))
        for bookname,book_url,author,book_abstract in zip(booknames,book_urls,authors,book_abstracts):
            item['bookname']=bookname
            item['book_url']=book_url
            item['author']=author.strip()
            item['book_abstract']=book_abstract.strip()
            # print(item['bookname'])
            yield item



