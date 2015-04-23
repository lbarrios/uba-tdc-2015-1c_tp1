#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scapy.all import *

def monitor_callback(pkt):
    print pkt.show()

sniff(prn=monitor_callback, store=0)