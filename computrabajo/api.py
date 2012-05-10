#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from urlparse import urljoin

from furl import furl
from lxml.html import parse


COUNTRIES = {
        'cl': 'http://www.computrabajo.cl/',
        'es': 'http://www.computrabajo.es/',
        'cr': 'http://www.computrabajo.co.cr/',
        'ar': 'http://www.computrabajo.com.ar/',
        'mx': 'http://www.computrabajo.com.mx/',
        'pe': 'http://www.computrabajo.com.pe/',
        've': 'http://www.computrabajo.com.ve/',
        'bo': 'http://www.bo.computrabajo.com/',
        'co': 'http://www.computrabajo.com.co/',
        'cu': 'http://www.cu.computrabajo.com/',
        'ec': 'http://www.computrabajo.com.ec/',
        'sv': 'http://www.sv.computrabajo.com/',
        'gt': 'http://www.gt.computrabajo.com/',
        'hn': 'http://www.hn.computrabajo.com/',
        'ni': 'http://www.ni.computrabajo.com/',
        'pa': 'http://www.computrabajo.com.pa/',
        'py': 'http://www.py.computrabajo.com/',
        'pr': 'http://www.computrabajo.com.pr/',
        'do': 'http://www.computrabajo.com.do/',
        'uy': 'http://www.uy.computrabajo.com/',
        }


class Search(object):

    def __init__(self, query, country):
        self.query = query
        self.country = country
        self.url = self._endpoint.url
        self.html = urllib.urlopen(self.url).read()
        self.__doc = parse(self.url).getroot()


    @property
    def _endpoint(self):
        f = furl(COUNTRIES.get(self.country)).join('bt-ofrlistado.htm')
        f.args['BqdPalabras']= self.query
        return f

    def descriptions(self):
        return [d.text_content() for d in self.__doc.xpath('//td/p/font')]

    def positions(self):
        return [c.text_content() for c in self.__doc.xpath('//td/font/b//a')]

    def links(self):
        return [urljoin(self.url, link.get('href')) for link in self.__doc.xpath('//td/font/b//a')]

    def jobs(self):
        # TODO: Clean this
        return [
                {'position': position, 'description': description, 'link': link }
                for position, description, link in zip(self.positions(), self.descriptions(), self.links())
                ]


