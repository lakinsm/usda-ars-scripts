#!/usr/bin/env python

import sys


def separate_xml(file, out_dir):
    with open(file, 'r') as f:
        data = f.read().split('\n')
        num = 0
        for line in data:
            if line.startswith('<?xml version') and num == 0:
                out = open(out_dir + '/gbk_' + str(num) + '.xml', 'w')
                num += 1
            elif line.startswith('<?xml version') and num > 0:
                out.close()
                num += 1
                out = open(out_dir + '/gbk_' + str(num) + '.xml', 'w')
            out.write('{}\n'.format(line))
        out.close()


if __name__ == '__main__':
    separate_xml(sys.argv[1], sys.argv[2])
