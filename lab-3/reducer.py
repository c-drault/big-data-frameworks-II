#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin :
  # remove leading and trailing white space
  line = line.strip()
  
  # parse the input we got from mapper.py
  word, count = line.split('\t', 1)
  
  # convert count (currently a string) to int
  # @TODO
  try:
    count = int(count)
  except ValueError:
    continue
  
  # this IF-switch only works because Hadoop sortsmap output
  # by key (here: word ) before it is passed to the reducer
  if current_word == word:
    current_count += count
  else:
    if current_word:
      print '%s\t%s' % (current_word, current_count)
    current_word = word
    current_count = count
  
  # do not forget to output the last word if needed !
  if current_word:
    print '%s\t%s' % (current_word, current_count)
