# coding=utf-8
import lxml.html
import math


class ParserTileInfo(object):
    def __init__(self, html_text):
        self.html = lxml.html.document_fromstring(html_text)

    xpath_list = {
        'fabric_title': '//*[@id="form_add"]/table/tr/td[3]/a[1]/text()',
        'country_name': '//*[@id="form_add"]/table/tr/td[3]/a[2]/text()',
        'collection_title': '//*[@id="form_add"]/table//tr/td[3]/a[3]/text()',
        'size_tile': '//*[@id="form_add"]/table/tr/td[3]/text()[4]',
        'surface': '//*[@id="form_add"]/table/tr/td[3]/a[6]/text()',
        'price': '//*[@id="form_add"]/table/tr/td[3]/span/text()',
        'unit_measure': '//*[@id="form_add"]/table/tr/td[3]/text()[9]',
        'designation': '//*[@id="form_add"]/table/tr/td[3]/a[4]'
    }

    def __parser_field_tile(self, xpath):
        result = self.html.xpath(xpath)
        if isinstance(result, list):
            result = result[0]
        return result

    def parser_fabric(self):
        fabric_title = self.__parser_field_tile(self.xpath_list['fabric_title'])
        return fabric_title

    def parser_country(self):
        country_name = self.__parser_field_tile(self.xpath_list['country_name'])
        return country_name

    def parser_collection(self):
        collection_title = self.__parser_field_tile(self.xpath_list['collection_title'])
        return collection_title

    def parser_size(self):
        container = self.__parser_field_tile(self.xpath_list['size_tile'])
        size = container.split(':')[1]
        return size.strip()

    def parser_surface(self):
        surface = self.__parser_field_tile(self.xpath_list['surface'])
        return surface

    def parser_price(self):
        price = self.__parser_field_tile(self.xpath_list['price'])
        price = float(price.replace(',', '.'))
        price = math.ceil(price)
        return int(price)

    def parser_unit_measure(self):
        container = self.__parser_field_tile(self.xpath_list['unit_measure'])
        unit_measure = container.split('/')
        unit_measure = unit_measure[1].strip()
        return unit_measure

    def parser_designation(self):
        container = self.__parser_field_tile(self.xpath_list['designation'])
        designation = container.text
        for elem in container.itersiblings():
            if elem.tag == u'br':
                break
            designation += u', ' + unicode(elem.text)
        return designation




