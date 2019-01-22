# -*- coding: utf-8 -*-
import json
import scrapy




class WizzMapSpider(scrapy.Spider):
    name = 'wizz_map'
    allowed_domains = ['wizzair.com']
    start_urls = [
        'https://be.wizzair.com/9.4.0/Api/asset/map?languageCode=en-gb&forceJavascriptOutput=true'
    ]


    def stripData(self, jsonInput):
        data = {}
        for city in jsonInput:
            code = city["iata"]
            data[code] = {
                "name": city["shortName"],
                "country": city["countryName"],
                "connections": [i["iata"] for i in city["connections"]],
                "prices": {}
            }

        return data


    def parse(self, response):
        # Parse this JS file to only get the
        """
                wizz = window.wizz || {};
                wizz.cities = [{"iata": "TIA",
                    "longitude": 19.720555555555553,
                ...
        """
        r = response.body_as_unicode().split("=")[2]

        # Also remove the trailing semicolon
        r = r[:-1]

        # Store the list
        data = json.loads(r)
        with open("map_parsed_no.json", "w") as f:
            json.dump(data, f)

        with open("map_parsed_yes.json", "w") as f:
            json.dump(self.stripData(data), f)

        # with open("map.json") as f:
        #     map = json.load(f)

