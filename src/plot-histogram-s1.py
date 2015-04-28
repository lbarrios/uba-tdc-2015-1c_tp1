#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse, json, string, sys
from funciones import *

# parse the arguments
parser = argparse.ArgumentParser(description='Parsea un json e imprime un histograma')
parser.add_argument('-i', '--input-testname', required=True, type=file_json,
  help='nombre del testname (archivo json en la carpeta output)', metavar='FILE')
args = parser.parse_args()

output_file = replace_ext(args.input_testname,'histogram.png')

# parse the json input file
with open(args.input_testname) as f:
    data = json.loads(f.read())
symbol_information = data['symbol_information']
symbol_frequency = data['symbol_frequency']
source_entropy = data['source_entropy']

# generate plot data
import numpy as np
execfile('plot-functions.py')
symbols, information = zip(*(symbol_information.items()))
posicion_x = np.arange(len(symbols))
# x_labels = [sym if info < source_entropy else ''
            # for sym, info in symbol_information.items()]


def make_unused_letter():
    unused_letters = list(string.ascii_uppercase)
    unused_letters.reverse()
    def unused_letter():
        return unused_letters.pop()
    return unused_letter

unused_letter = make_unused_letter()
        
x_labels = [unused_letter() if info < source_entropy else ''
            for sym, info in symbol_information.items()]
            
# colors = ['r' if info < source_entropy else 'b'
            # for sym, info in symbol_information.items()]

# plot
import matplotlib.pyplot as plt
width = 0.5
plt.bar(posicion_x, information, align='center', width=width)
plt.xticks(posicion_x, x_labels, rotation=0)
plt.xlabel('MAC Address')
plt.title(u'Información segun MAC Address')

plt.plot([0 - width / 2.0, posicion_x[-1] + width / 2.0], [source_entropy, source_entropy], color='red', lw=2)
plt.savefig(output_file)
