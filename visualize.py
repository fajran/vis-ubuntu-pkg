#!/usr/bin/python

import sys
import json

import config

def create_table(data):
    code = {}
    for arch in data:
        if not arch in data:
            continue

        out = []

        a = out.append
        a('google.visualization.arrayToDataTable([')

        line = '  ["Release"'
        for section in config.SECTIONS:
            line += ', "%s"' % section
        line += '],'
        a(line)

        for dist in config.DISTS:
            if not dist in data[arch]:
                continue

            line = '  ["%s"' % dist

            for section in config.SECTIONS:
                value = 0
                if section in data[arch][dist]:
                    value = data[arch][dist][section]

                line += ', %d' % value

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
    print 'function getData() {'
    print 'var data = {};'
    visualize_packages(data)
    visualize_size(data)
    print 'return data;'
    print '}'

def main():
    inp = sys.argv[1]
    data = json.load(open(inp))

    visualize(data)

if __name__ == '__main__':
    main()

