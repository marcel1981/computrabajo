#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib

import fudge
# from py.test import skip

from computrabajo.api import Search


HERE = os.path.abspath(os.path.dirname(__file__))


class TestComputrabajoListadoSearch(object):

    def setup_method(self, method):
        html = open(os.path.join(HERE, 'html/listado.html'))
        fake = fudge.Fake('urlopen', callable=True).with_args('http://www.computrabajo.com.pe/bt-ofrlistado.htm?BqdPalabras=python').returns(html)
        with fudge.patched_context(urllib, 'urlopen', fake):
            self.search = Search('python', country='pe')

    def test_endpoint_url(self):
        assert self.search._endpoint.url == 'http://www.computrabajo.com.pe/bt-ofrlistado.htm?BqdPalabras=python'

    def test_titles_listado(self):
        titles = self.search.titles()
        assert titles == \
                [u'LAMP Python Developer',
                 u'QA Engineer',
                 u'Soporte en Mantenimiento de Software',
                 u'Programador T\xe9cnico (PRO - T)',
                 u'It Support Linux',
                 u'Web Developer',
                 u'Programador T\xe9cnico - C\xf3digo (PRO - T)',
                 u'Practicante Sistemas/Programaci\xf3n',
                 u'Programador PHP',
                 u'Docentes Desarrollo WEB 2.0',
                 u'Se requiere practicante de sistemas',
                 u'\xa1Program\xe1 en PHP desde las monta\xf1as!']

    def test_links_listado(self):
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
        # skip('Sorry no yet')
        desc = self.search.descriptions()
        assert desc[0] == \
                    u'Taller Technologies Per\xfa is part of the Talent Trust group, based in San Francisco with operations in Latin America, Asia and Europe. We are seeking skilled and self-motivated\nindividuals to develop and support enterprise web applications for our US client.\n\nJob Description\n- Design, develop and support web sites using LAMP/Python, JQuery, JavaScript, YUI and HTML\n- Work with Systems Architects at our US locations (some travel may be required) and support client/owners of hosted web sites for campaign ..... (contin\xfaa)'
        assert desc[-1] == \
                    u'\xbfEst\xe1s buscando un cambio laboral y de aire? En Waragon tenemos la oferta justa para ofrecerte!\nEstamos buscando programadores PHP SemiSenior, Senior y Tech Leads, para incorporarse al equipo de desarrollo de la plataforma de compras colectivas m\xe1s importante a nivel mundial.\n\nLas oficinas de la empresa se encuentran ubicadas en Santiago de Chile, Chile, y a los candidatos seleccionados se les ofrecer\xe1 un "plan starter" para la relocalizaci\xf3n a la ciudad.\n\nNos orientamos a personas con experiencia laboral o ..... (contin\xfaa)'


