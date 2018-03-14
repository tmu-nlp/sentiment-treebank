#!/usr/bin/python

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--lexicon", help="Lexicon file")
parser.add_argument("-c", "--corpus", help="KyTea segmented corpus")
args = parser.parse_args()

if not args.lexicon or not args.corpus:
  print("You must specify both lexicon (-l) and corpus (-c).")
  sys.exit()

id2word = {}
for line in open(args.lexicon):
  line = line.strip()
  (word, wid) = line.split()
  id2word[wid] = word

for line in open(args.corpus):
  line  = line.strip()
  (pid, cat, tag1, tag2, tag3, phrase) = line.split("\t", 5)
  wids = phrase.split()
  words = []
  for wid in wids:
    try:
      words.append(id2word[wid])
    except KeyError:
      print("Key not found in id2word.")
  print("{}\t{}\t{}\t{}\t{}\t{}".format(pid, cat, tag1, tag2, tag3, " ".join(words)))
