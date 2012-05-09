
Computrabajo
============

A pseudo-api for computrabajo.com

::

    >>> from computrabajo.api import Search
    >>> labs = Search('laboratorio')
    >>> labs.jobs()
    [
      {'title': 'Asistente de laboratorio secreto',
       'description': 'Cientifico Loco busca aistente para lab...'
       'link': 'http://www.computrabajo.com.pe/bt-ofrd-loco-0042.htm'},
      {'title': 'Auxiliar laboratorio',
      ...
    ]


