import json
import sys
import matplotlib.pyplot as plt
import numpy as np

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    data = json.loads(f.read())

symbol_information = data['symbol_information']
source_entropy = data['source_entropy']
symbols, information = zip(*(symbol_information.items()))

protocol_title = {
    '2048': 'IPv4',
    '34525': 'IPv6',
    '2054': 'ARP'
}

protocols = [protocol_title[s] for s in symbols]

posicion_x = np.arange(len(protocols))

width = 0.5

plt.bar(posicion_x, information, align='center', width=width)
plt.xticks(posicion_x, protocols)
plt.xlabel('Protocolo')
plt.title('Informacion segun protocolo')

plt.plot([0 - width / 2.0, posicion_x[-1] + width / 2.0], [source_entropy, source_entropy], color='red', lw=2)

plt.savefig(output_file)
