#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scapy.all import *
import math
import json
import sys

output_file = sys.argv[1]

pkts = sniff(offline='../output/out.pcap')

symbol_count = {}
pkts_count = 0

for pkt in pkts:
    try:
        pkt_type = pkt.type
    except AttributeError:
        pass
    else:
        pkts_count += 1
        if pkt_type not in symbol_count:
            symbol_count[pkt_type] = 0
        symbol_count[pkt_type] += 1

symbol_freq = {k: v/float(pkts_count) for k,v in symbol_count.items()}
symbol_information = {k: -(math.log(v, 2)) for k,v in symbol_freq.items()}
source_entropy = sum({k: (v * symbol_information[k]) for k,v in symbol_freq.items()}.values())

result = {
    'symbol_freq': symbol_freq,
    'symbol_information': symbol_information,
    'source_entropy': source_entropy
}

with open(output_file, 'w') as f:
    f.write(json.dumps(result))
