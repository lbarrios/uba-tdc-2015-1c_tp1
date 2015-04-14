from scapy.all import *
import math

symbol_count = {}
total_pkts = 100

def monitor_callback(pkt):
    try:
        pkt_type = pkt.type
    except AttributeError:
        print '***'
        print 'el siguiente paquete no tiene pkt.type'
        print pkt.show()
        print '***'
    else:
        if pkt_type not in symbol_count:
            symbol_count[pkt_type] = 0
        symbol_count[pkt_type] += 1

sniff(prn=monitor_callback, store=0, count=total_pkts)

print symbol_count

symbol_freq = {k: v/float(total_pkts) for k,v in symbol_count.items()}

print symbol_freq

symbol_information = {k: -(math.log(v, 2)) for k,v in symbol_freq.items()}

print symbol_information

source_entropy = sum({k: (v * symbol_information[k]) for k,v in symbol_freq.items()}.values())

print source_entropy
