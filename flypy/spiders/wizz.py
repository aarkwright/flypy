# -*- coding: utf-8 -*-
import scrapy
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from fake_useragent import UserAgent

from random import choice


class WizzSpider(scrapy.Spider):
    name = 'wizz'
    allowed_domains = ['wizzair.com', 'be.wizzair.com']
    start_urls = ["https://wizzair.com/"]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        # Get ak_bmsc cookie
        url = "https://be.wizzair.com/9.4.2/Api/information/buildNumber"

        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        session.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Origin": "https://wizzair.com",
            "Referer": "https://wizzair.com/",
            "User-Agent": UserAgent().random
        }
        r = session.get(url=url)
        print(r)

        requests.request(method="GET", url="https://be.wizzair.com/9.4.2/Api/information/buildNumber", headers=headers)








        ### DEBUG
        # url = "https://be.wizzair.com/9.4.2/Api/search/search"
        # url_get_flight_dates = "https://be.wizzair.com/9.4.2/Api/search/flightDates?departureStation=CLJ&arrivalStation=EIN&from=2019-01-31&to=2019-03-31"
        #
        # ak_bmsc = "ak_bmsc=EE64806453C980085A5D045D9BE509ED02112B7C803100004609475CEC8EF82C~plPpYVy4qKtwXRtc5PiQw+b6n/3sqxR0mXeT0ZYxZJmmkjNrRRkzV9wCOJCqCwbDkdT1y38LzVELhvrgGkJY4Iyxj2dG/yll/R9wYbEY1ouweX6dmN7axfCOxd/cLG99KfGYWoDFTGtsbbpdaegcIr59lLWBkSdCi8YO2z4PRmXlzLTc/dUdiM76zg3FLUaP2fm7uuzFIkVARhoNTd+DjTuvsW2f0rtl9IYSktIaCYvQg=; expires=Tue, 22 Jan 2019 14:15:02 GMT; max-age=7200; path=/; domain=.wizzair.com; HttpOnly"
        # headers = {
        #     "Origin": "https://wizzair.com",
        #     "Referer": "https://wizzair.com",
        #     "Accept": "*/*",
        #     "Accept-Encoding": "gzip, deflate, br",
        #     "Accept-Language": "en-US,en;q=0.9"
        # }
        #
        # payload = {
        #     "adultCount": 1,
        #     "childCount": 0,
        #     "dayInterval": 3,
        #     "wdc": "false",
        #     "flightList": [
        #         {
        #             "departureStation": "CLJ",
        #             "arrivalStation": "EIN",
        #             "date": "2019-01-31"
        #         }
        #     ]
        # }
        #
        #
        # x = s.options(url=url)
        # s.request(method="OPTIONS", url=url, headers=json.dumps(headers), data=payload)
        # print(x)



# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

# def parse(self, response):
#     for quote in response.css('div.quote'):
#         yield {
#             'text': quote.css('span.text::text').extract_first(),
#             'author': quote.css('small.author::text').extract_first(),
#             'tags': quote.css('div.tags a.tag::text').extract(),
#         }

# def parse(self, response):
#     page = response.url.split("/")[-2]
#     filename = 'quotes-%s.html' % page
#     with open(filename, 'wb') as f:
#         f.write(response.body)
#     self.log('Saved file %s' % filename)
