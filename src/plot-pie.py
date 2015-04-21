import json
import sys
import matplotlib.pyplot as plt

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    data = json.loads(f.read())

symbol_freq = data['symbol_freq']
symbols, freqs = zip(*(symbol_freq.items()))

protocol_title = {
    '2048': 'IPv4',
    '34525': 'IPv6',
    '2054': 'ARP'
}

protocols = [protocol_title[s] for s in symbols]

plt.pie(freqs, labels=protocols, title='Frecuencias de distintos protocolos')
plt.savefig(output_file)
