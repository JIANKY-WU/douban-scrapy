# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time, requests
from multiprocessing import Process
import pymongo
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from douban.settings import COOKIES
import cv2
import numpy as np
from scrapy import signals
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait

from douban import douban
from douban.settings import *
import logging


class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumMiddleware(object):

    def process_request(self,request,spider):
        global COOKIES
        # p=Process(target=douban.run,args=(request.url,))
        # p.start()
        # p.join()
        url='https://www.douban.com/'
        if request.url==url:
            cookies=douban.run(request.url)
            if cookies:
                request.cookies=cookies
                COOKIES=cookies
        if COOKIES:
            request.cookies=COOKIES


    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.wait = wait.WebDriverWait(self.driver, 10)

    # def get_distance(self):
    #     bkg = cv2.imread('bkg.png', 0)
    #     block = cv2.imread('block.png', 0)
    #     cv2.imwrite('template.jpg', bkg)
    #     cv2.imwrite('block.jpg', block)
    #     block = cv2.imread('block.jpg',0)
    #     block = cv2.cvtColor(block, cv2.COLOR_BAYER_BG2GRAY)
    #     block = abs(255 - block)
    #     cv2.imwrite('block.jpg', block)
    #     block = cv2.imread('block.jpg')
    #     template = cv2.imread('template.jpg')
    #     result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)
    #     x, y = np.unravel_index(result.argmax(), result.shape)
    #     y=y-72
    #     print(y)
    #     return y, template
    #
    # def get_track(self, distance):
    #     v0 = 0
    #     mid = distance / 5 * 4
    #     v = 0
    #     t = 0.3
    #     tracks = []
    #     current = 0
    #     while current < distance:
    #         if current < mid:
    #             a = 2
    #         else:
    #             a = -3
    #         v0 = v
    #         s = v0 * t + 0.5 * a * t * t
    #         current = s + current
    #         tracks.append(s)
    #         v = v0 + a * t
    #     return tracks
    #
    # def process_request(self, request, spider):
    #     url = 'https://www.douban.com/'
    #     if request.url == url:
    #         self.driver.get(url)
    #         self.driver.switch_to_frame(0)
    #         diot = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    #         diot.click()
    #         username = self.driver.find_element_by_id('username')
    #         username.send_keys(USERNAME)
    #         password = self.driver.find_element_by_id('password')
    #         password.send_keys(PASSWORD)
    #         buttom = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a')
    #         buttom.click()
    #         self.driver.implicitly_wait(5)
    #         frame = self.driver.find_element_by_xpath('//*[@id="TCaptcha"]/iframe')
    #         self.driver.switch_to_frame(frame)
    #
    #         slidebkg = self.driver.find_element_by_id('slideBkg').get_attribute('src')
    #         slideblock = self.driver.find_element_by_id('slideBlock').get_attribute('src')
    #         print(slidebkg)
    #         time.sleep(2)
    #         Bkg = requests.get(slidebkg)
    #         Block = requests.get(slideblock)
    #         with open('bkg.png', 'wb') as f:
    #             f.write(Bkg.content)
    #         with open('block.png', 'wb') as f:
    #             f.write(Block.content)
    #
    #         distance, template = self.get_distance()
    #         tracks = self.get_track(distance)
    #
    #         block = self.driver.find_element_by_id('tcaptcha_drag_thumb')
    #         action = ActionChains(self.driver)
    #         action.click_and_hold(on_element=block).perform()
    #         for track in tracks:
    #             action.move_by_offset(xoffset=track, yoffset=0).perform()
    #         time.sleep(0.5)
    #         action.release(on_element=block).perform()

            # self.driver.switch_to_default_content()

class User_AgetnMiddleware():


    def process_request(self,request,spider):
        headers={
            'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',

        }
        if headers:
            # request.headers.setdefault('User-Agent',headers['User_Agent'])
            request.headers['User-Agent']=headers['User_Agent']


class CookiesMiddleware():

    def process_request(self,request,spider):
        if COOKIES:
            request.cookies=COOKIES


