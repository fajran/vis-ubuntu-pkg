#!/usr/bin/python

import sys
import json

import config

def create_table(data):
    code = {}
    for arch in data:
        out = []

        a = out.append
        a('google.visualization.arrayToDataTable([')

        line = '  ["Release"'
        for section in config.SECTIONS:
            line += ', "%s"' % section
        line += '],'
        a(line)

        for dist in config.DISTS:
            line = '  ["%s"' % dist

            for section in config.SECTIONS:
                line += ', %d' % data[arch][dist][section]

            line += '],'
            a(line)

        a(']);')

        code[arch] = '\n'.join(out)

    return code

def visualize_packages(data):
    table = create_table(data['packages'])

    print 'data["packages"] = {};';
    for arch in config.ARCHS:
        print 'data["packages"]["%s"] = %s' % (arch, table[arch])

def visualize_size(data):
    table = create_table(data['sizes'])

    print 'data["sizes"] = {};';
    for arch in config.ARCHS:
        print 'data["sizes"]["%s"] = %s' % (arch, table[arch])

def visualize(data):
    print 'var data = {};'
    visualize_packages(data)
    visualize_size(data)

def main():
    inp = sys.argv[1]
    data = json.load(open(inp))

    visualize(data)

if __name__ == '__main__':
    main()

