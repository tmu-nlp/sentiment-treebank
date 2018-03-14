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

word2id = {}
for line in open(args.lexicon):
  line = line.strip()
  (word, wid) = line.split()
  word2id[word] = wid

for line in open(args.corpus):
  line  = line.strip()
  (pid, cat, tag1, tag2, tag3, phrase) = line.split("\t", 5)
  words = phrase.split()
  ids  = []
  for word in words:
    try:
      ids.append(word2id[word])
    except KeyError:
      print("Key not found in word2id.")
      print(word)
  print("{}\t{}\t{}\t{}\t{}\t{}".format(pid, cat, tag1, tag2, tag3, " ".join(ids)))
