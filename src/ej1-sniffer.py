#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, sys, os

def file_ok(x):
  if '/' in x or '.' in x:
    parser.error('''Invalid testname.
      Please, don't use "/" nor "." in your testname.
      Valid testnames, ie: "shopping1", "trabajo5", "casa2", etc.''')
  y = '../output/'+x+'.pcap'
  if os.path.isfile(y) or os.path.exists(y):
    parser.error('''The file {} already exists.
      Please, use a non-existent path'''.format(y))
  return y

parser = argparse.ArgumentParser(description='''network traffic capture 
  (a.k.a. sniffing) tool.''')
parser.add_argument('-t', '--max-running-time', required=True, type=int, 
  help='max running time in seconds')
parser.add_argument('-p', '--max-captured-packets', required=True, type=int, 
  help='max captured packets')
parser.add_argument('-o', '--output-testname', required=True, type=file_ok,
  help='non-existent testname to save the sniffing output', metavar='FILE')

args = parser.parse_args()

print '''capturing packets with parameters:
\tmax_running_time=%s\n\tmax_captured_packets=%s\n\toutput_testname=%s'''%(
  args.max_running_time, args.max_captured_packets, args.output_testname)

from scapy.all import sniff,wrpcap
pkts = sniff(count=args.max_captured_packets,timeout=args.max_running_time)

if pkts == []:
  print "sorry, no packets captured :(\ntry with a higher running time"
else:
  wrpcap(args.output_testname,pkts)
  print 'output saved in file {}'.format(args.output_testname)