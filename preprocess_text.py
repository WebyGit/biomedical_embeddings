#!/usr/bin/env python
# -*- coding: utf8 -*-

import re, sys, nltk.data
from nltk.tokenize import WordPunctTokenizer

tokenize = WordPunctTokenizer().tokenize

NOT_INTERESTING_CHARACTERS_RE = re.compile(r'[@#$%^&*()\-–_=+~`"№;:*\\/|\',\.<>]')
NUMBER_RE = re.compile(r'^[\d\.]+$')
PRINT_EACH = 10000

def good_token(token):
    return len(token) > 2 and not NUMBER_RE.match(token)

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file, 'r', encoding='utf8') as in_f:
    with open(out_file, 'w', encoding='utf8') as out_f:
        for line_i, line in enumerate(in_f):
            line = NOT_INTERESTING_CHARACTERS_RE.sub(' ', line.lower())
            line = line.strip()

            if not line:
                continue

            tokens = list(filter(good_token, tokenize(line)))

            if len(tokens) <= 1:
                continue

            out_f.write(' '.join(tokens) + '\n')

            if line_i % PRINT_EACH == 0:
                print('{} lines processed'.format(line_i))
