# coding=utf-8
import lxml.html


class ParserTileInfo(object):
    def __init__(self, html_text):
        self.html = lxml.html.document_fromstring(html_text)
