
Computrabajo
============

.. image:: https://secure.travis-ci.org/marsam/computrabajo.png?branch=master

A pseudo-api for computrabajo.com

Intalling
---------
::

    $ pip install computrabajo


Using
-----

1. Using the pseudo-API::

    >>> from computrabajo.api import API
    >>> ct = API('pe')
    >>> lab_jobs = ct.search('laboratorio')
    >>> lab_jobs  # doctest: +SKIP
    [
      Job(position='Asistente de laboratorio secreto',
          summary='Cientifico Loco busca asistente de laboratorio para conquistar el mundo... ',
          link='http://www.computrabajo.com.pe/bt-ofrd-loco-0042.htm'),
      Job(position='Auxiliar de laboratorio',
          summary='Laboratorio necesita auxiliar masoquista para... '
      ...
    ]
    >>> info = [job.information for job in lab_jobs]   # This will take some time
    >>> import json
    >>> with open('labs_jobs.json', 'w') as f:
    ...    json.dump(info, f, indent=2)
    ...
    >>>

2. Using from the command line::

    $ trabajo.py --country pe --term secretaria --format xlsx

   Now open the jobs.xlsx file.


*NOTE*: Don't run this file with *doctest*

