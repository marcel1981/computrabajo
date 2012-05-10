
Computrabajo
============

.. image:: https://secure.travis-ci.org/marsam/computrabajo.png?branch=master

A pseudo-api for computrabajo.com

::

    >>> from computrabajo.api import Search
    >>> labs = Search('laboratorio', country='pe')
    >>> labs.jobs()
    [
      {'position': 'Asistente de laboratorio secreto',
       'description': 'Cientifico Loco busca aistente para lab...'
       'link': 'http://www.computrabajo.com.pe/bt-ofrd-loco-0042.htm'},
      {'position': 'Auxiliar laboratorio',
      ...
    ]


