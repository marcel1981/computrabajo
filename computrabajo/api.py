#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import urllib
from urlparse import urljoin
from collections import namedtuple

# from furl import furl
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


class ComputrabajoError(Exception):
    pass


class API:
    def __init__(self, country):
        if COUNTRIES.get(country):
            self.country = country
            self.homepage = COUNTRIES[country]
        else:
            raise ComputrabajoError,  "No computrabajo site in that country"

    def search(self, query, pages=1):
        url = urljoin(self.homepage, 'bt-ofrlistado.htm?BqdPalabras={0}'.format(query))
        result = CrawlPage(url).get_jobs()
        return result


class CrawlPage:

    def __init__(self, url):
        self.url = url
        self._root = parse(self.url).getroot()

    def get_jobs(self):
        summaries = [s.text_content() for s in self._root.xpath('//td/p/font')]
        positions = [p.text_content() for p in self._root.xpath('//td/font/b//a')]
        links     = [urljoin(self.url, l.get('href')) for l in self._root.xpath('//td/font/b//a')]
        return [
                Job(**{'position': position, 'summary': summary, 'link': link }) 
                for position, summary, link in zip(positions, summaries, links)
                ]


class Job(namedtuple('Job',['position', 'link', 'summary'])):
    __slots__ = ()

    @property
    def information(self):
        result = {}
        root = parse(self.link).getroot()
        result['description'] = root.xpath('//tr[6]/td[1]/p')[0].text_content()
        result['date']        = root.xpath('//tr[8]/td[2]/font[count(*)=0]')[0].text_content()
        result['location']    = root.xpath('//tr[9]/td[2]/font')[0].text_content()
        result['department']  = root.xpath('//tr[10]/td[2]/font[count(*)=0]')[0].text_content()
        result['salary']      = root.xpath('//tr[11]/td[2]/font[count(*)=0]')[0].text_content()
        result['begin']       = root.xpath('//tr[12]/td[2]/font')[0].text_content()
        result['duration']    = root.xpath('//tr[13]/td[2]/font')[0].text_content()
        result['job_type']    = root.xpath('//tr[14]/td[2]/font')[0].text_content()
        result['solicitudes'] = root.xpath('//tr[15]/td[2]/font')[0].text_content()
        result['empresa']     = root.xpath('//tr[16]/td[2]/font/a')[0].text_content()
        result['contact']     = root.xpath('//tr[17]/td[2]/font')[0].text_content()
        result['phone']       = root.xpath('//tr[18]/td[2]/font')[0].text_content()
        result['fax']         = root.xpath('//tr[19]/td[2]/font')[0].text_content()
        result['email']       = root.xpath('//tr[20]/td[2]/img')[0].get('src')
        return result

    def __str__(self):
        return 'Job: {0}'.format(self.position)

