#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from urlparse import urljoin

from furl import furl
from lxml.html import parse
from bs4 import BeautifulSoup

from .helpers import clean_html


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
        self.__setup(query, country)

    def __setup(self, query, country):
        endpoint = furl(COUNTRIES.get(country)).join('bt-ofrlistado.htm')
        endpoint.args['BqdPalabras']= query
        self.url = endpoint.url
        self.html = urllib.urlopen(self.url).read()
        self.__doc = parse(self.url).getroot()


    def descriptions(self):
        soup = BeautifulSoup(self.html)
        content = soup.find('table', {'cellpadding': '2'})
        ajobs = [ c.find('p',{'align': 'justify'}) for c in content.findAll('td') \
                if c.find('p',{'align': 'justify'}) != None ]
        jobs = (clean_html(str(job)) for job in ajobs)
        # the following deletes the warning messages
        jobs.next()
        jobs.next()
        return jobs

    def titles(self):
        """Return a generator of the jobs titles"""
        soup = BeautifulSoup(self.html)
        content = soup.find('table', {'cellpadding': '2'})
        titles = [ c.find('a') for c in content.findAll('td') if c.find('a') != None]
        return (clean_html(str(title)) for title in titles)

    def links(self):
        links = [c.get('href') for c in self. __doc.xpath('//td/font/b//a')]
        return [urljoin(self.url, link) for link in links]

    def jobs(self):
        # TODO: Clean this
        return [
                {'title': title, 'description': description, 'link': link }
                for title, description, link in zip(self.titles(), self.descriptions(), self.links())
                ]


