#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib

import fudge
from py.test import skip

from computrabajo.api import Search


HERE = os.path.abspath(os.path.dirname(__file__))


class TestComputrabajoListadoSearch(object):

    def setup_method(self, method):
        html = open(os.path.join(HERE, 'html/listado.html'))
        fake = fudge.Fake('urlopen', callable=True).with_args('http://www.computrabajo.com.pe/bt-ofrlistado.htm?BqdPalabras=python').returns(html)
        with fudge.patched_context(urllib, 'urlopen', fake):
            self.search = Search('python', country='pe')

    def test_endpoint_url(self):
        assert self.search.endpoint.url == 'http://www.computrabajo.com.pe/bt-ofrlistado.htm?BqdPalabras=python'

    def test_titles_listado(self):
        titles = list(self.search.titles())
        assert titles == \
                ['LAMP  Python  Developer',
                'QA Engineer',
                'Soporte en Mantenimiento de Software',
                'Programador T\xc3\xa9cnico (PRO - T)',
                'It Support Linux',
                'Web Developer',
                'Programador T\xc3\xa9cnico - C\xc3\xb3digo (PRO - T)',
                'Practicante Sistemas/Programaci\xc3\xb3n',
                'Programador PHP',
                'Docentes Desarrollo WEB 2.0',
                'Se requiere practicante de sistemas',
                '\xc2\xa1Program\xc3\xa1 en PHP desde las monta\xc3\xb1as!',
                'Listado de empresas']

    def test_links_listado(self):
        # skip('Sorry no yet')
        links = self.search.links()
        assert links == ['http://www.computrabajo.com.pe/bt-ofrd-mmazan-21444.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-mmazan-64332.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-peruserversac-57184.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-primerospuestos-564692.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-avanticape-293068.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-mmazan-107220.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-obiettivolavoro-1365268.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-rudiyard-0.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-phantasia-50036.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-nexcorp-64332.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-andresweb-7148.htm?BqdPalabras=python',
                 'http://www.computrabajo.com.pe/bt-ofrd-waragoner-7148.htm?BqdPalabras=python']

    def test__listado(self):
        descriptions = self.search.descriptions()
        assert descriptions.next() == \
                'Taller Technologies Per\xc3\xba is part of the Talent Trust group, based in San Francisco with operations in Latin America, Asia and Europe. We are seeking skilled and self-motivated\nindividuals to develop and support enterprise web applications for our US client.\n\nJob Description\n- Design, develop and support web sites using LAMP/ Python , JQuery, JavaScript, YUI and HTML\n- Work with Systems Architects at our US locations (some travel may be required) and support client/owners of hosted web sites for campaign ..... (contin\xc3\xbaa)'


