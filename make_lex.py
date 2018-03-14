#!/usr/bin/pytnon
# cat tsukuba_corpus.txt | python make_lex.py

import sys

lex = {}

for line in sys.stdin:
  line  = line.strip()
  words = line.split()
  for word in words:
    lex[word] = 1

lex = sorted(lex.items())
wid = 0

for word in lex:
  print(word[0] + "\t" + str(wid))
  wid += 1
