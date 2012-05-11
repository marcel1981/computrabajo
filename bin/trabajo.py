#!/usr/bin/env python

import tablib
import argparse

from computrabajo.api import API


def command():
    parser = argparse.ArgumentParser(description='Get jobs from computrabajo.com')
    parser.add_argument('-c', '--country', dest='country', required=True, help='Set computrabajo country')
    parser.add_argument('-t', '--term', dest='term', required=True, help='Job term for looking for')
    parser.add_argument('-f', '--format', dest='format', default='xls', choices=['csv', 'json', 'yaml', 'xls'], help='Set the output file format')
    parser.add_argument('-o', '--output', dest='output', default='jobs', help='Set the output filename')

    args = parser.parse_args()
    api = API(args.country)
    jobs = api.search(args.term)
    data = tablib.Dataset()
    data.dict = [job.information for job in jobs]

    output_file = '{0}.{1}'.format(args.output, args.format)

    with open(output_file, 'wb') as f:
        f.write(getattr(data, args.format))


if __name__ == '__main__':
    command()
