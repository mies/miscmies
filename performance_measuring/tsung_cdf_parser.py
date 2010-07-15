#!/usr/bin/env python
import sys
import csv

REQUESTS_COLUMN = 2

def parse_log(filename, separator):
  """Parses Tsung's request.txt log file.
  
  This is the file generated in the 'data' dir after running 'tsung_stats.pl'
  The second column contains the requests and the log is delimited
  by whitespace.

  """

  for line in csv.reader(open(filename), delimiter=separator, 
      skipinitialspace=True):
        if line:
          yield line[REQUESTS_COLUMN]

def calculate_cdfs(response_times):
  """ Calculates the Cumulative distribution function for the response times."""
  prob = 0
  for time in response_times:
    prob += 1.0 / len(response_times)
    print "%.4f\t%.4f" % (prob, time)

def main(fd):
  """ Main entry point.

  Expects a filename (request.txt) as command line argument.
  Delimiter is set to whitespace (' ') by default.

  """
  response_times = []
  for line in parse_log(fd, ' '):
    if len(line.strip()):
      response_times.append(float(line.strip()))

  response_times.sort()
  calculate_cdfs(response_times)

if __name__ == '__main__':
  main(sys.argv[1])
