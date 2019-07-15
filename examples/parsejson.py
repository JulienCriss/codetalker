#!/usr/bin/env python
from __future__ import print_function

import os
import sys

from codetalker.contrib.json import loads
from codetalker.pgm.errors import ParseError, TokenError


def parse(text):
    try:
        print(loads(text))
    except (TokenError, ParseError) as e:
        if text:
            print(text.splitlines()[e.lineno - 1], file=sys.stderr)
        else:
            print(file=sys.stderr)
        print(' ' * (e.charno - 1) + '^', file=sys.stderr)
        print("Invalid Syntax:", e, file=sys.stderr)


if len(sys.argv) > 1:
    if not os.path.isfile(sys.argv[1]):
        print('Error: arg must be a file path')
        sys.exit(1)
    print('parsing file: %s' % (sys.argv[1],))
    parse(open(sys.argv[1]).read())
else:
    print('reading from stdin...')
    parse(sys.stdin.read())
