#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest

from computrabajo.api import API
from computrabajo.api import Job
from computrabajo.api import CrawlPage
from computrabajo.api import ComputrabajoError


HERE = os.path.abspath(os.path.dirname(__file__))


class TestComputrabajoAPI:
    def setup_method(self, method):
        pass

    def test_set_country_bolivia(self):
        api = API('bo')
        assert api.country == 'bo'
        assert api.homepage == 'http://www.bo.computrabajo.com/'

    def test_raise_exception_when_no_country(self):
        with pytest.raises(ComputrabajoError):
            API('cn')


class TestPageCrawl:
    def setup_method(self, method):
        # TODO: Fix this
        html = open(os.path.join(HERE, 'html/listado.html'))
        self.cpage = CrawlPage(html)
        self.cpage.url = 'http://www.computrabajo.com.pe/bt-ofrlistado.htm?BqdPalabras=python'

    def test_pagecrawl_get_jobs(self):
        # pytest.skip('Sorry no yet')
        jobs = self.cpage.get_jobs()
        first_job = jobs[0]
        last_job = jobs[-1]
        assert first_job.position == u'LAMP Python Developer'
        assert first_job.link     == 'http://www.computrabajo.com.pe/bt-ofrd-mmazan-21444.htm?BqdPalabras=python'
        assert first_job.summary  == \
                    u'Taller Technologies Per\xfa is part of the Talent Trust group, based in San Francisco with operations in Latin America, Asia and Europe. We are seeking skilled and self-motivated\nindividuals to develop and support enterprise web applications for our US client.\n\nJob Description\n- Design, develop and support web sites using LAMP/Python, JQuery, JavaScript, YUI and HTML\n- Work with Systems Architects at our US locations (some travel may be required) and support client/owners of hosted web sites for campaign ..... (contin\xfaa)'

        assert last_job.position == u'\xa1Program\xe1 en PHP desde las monta\xf1as!'
        assert last_job.link     == 'http://www.computrabajo.com.pe/bt-ofrd-waragoner-7148.htm?BqdPalabras=python'
        assert last_job.summary  == \
                    u'\xbfEst\xe1s buscando un cambio laboral y de aire? En Waragon tenemos la oferta justa para ofrecerte!\nEstamos buscando programadores PHP SemiSenior, Senior y Tech Leads, para incorporarse al equipo de desarrollo de la plataforma de compras colectivas m\xe1s importante a nivel mundial.\n\nLas oficinas de la empresa se encuentran ubicadas en Santiago de Chile, Chile, y a los candidatos seleccionados se les ofrecer\xe1 un "plan starter" para la relocalizaci\xf3n a la ciudad.\n\nNos orientamos a personas con experiencia laboral o ..... (contin\xfaa)'

class TestJob:
    def setup_method(self, method):
        self.job = Job('Asistente laboratorio', open('tests/html/job.html'), 'Científico Loco busca ...')

    def test_job_information_crawl(self):
        assert self.job.information == {
                'begin': '01/07/2008',
                'contact': 'Miguel Venegas',
                'date': '20 de abril de 2012',
                'department': 'Lima',
                'description': u'Empresa que brinda servicios de comunicaciones a nivel nacional e internacional, requiere personal con especialidad en plataforma Linux, principalmente en servicios de Internet (correo, proxy, firewall, etc.). Requisitos: - Buena presencia. - Buen trato y desenvolvimiento (indispensable). - Conocimientos de Linux y de servicios sobre \xe9sta plataforma (indispensable). - Conceptos claros de Networking. - Disponibilidad inmediata, A TIEMPO COMPLETO.',
                'duration': 'Estable',
                'email': 'correoe.cgi?ofrd=cyberuser-0&1336706158',
                'empresa': 'Cyberline SRL',
                'fax': '',
                'job_type': ' Tiempo Completo',
                'location': 'Lima',
                'phone': '',
                'salary': 'a tratar',
                'solicitudes': u'enviar curr\xedculum por correo electr\xf3nico'}

