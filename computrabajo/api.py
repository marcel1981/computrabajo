#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from urlparse import urljoin

# from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup

from .helpers import clean_html


class Search(object):
    url = 'http://www.computrabajo.com.pe/bt-ofrlistado.htm'

    def __init__(self, query, country='pe'):
        self._search(query)
        self.country = country

    def _search(self, query):
        params = urllib.urlencode({'BqdPalabras': query})
        self.html = urllib.urlopen(self.url, params).read()
        return

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
        soup = BeautifulSoup(self.html)
        content = soup.find('table', {'cellpadding': '2'})
        links = [c.find('a').get('href') for c in content.findAll('td') if c.find('a') != None]
        return (urljoin(self.url, link) for link in links)

    def jobs(self):
        # TODO: Clean this
        return [
                {'title': title, 'description': description, 'link': link }
                for title, description, link in zip(self.titles(), self.descriptions(), self.links())
                ]


