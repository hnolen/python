#! /usr/bin/env python3

import argparse
import gzip
import Bio.SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('i', type=str, help='input path')
parser.add_argument('o', type=str, help='header output file')
parser.add_argument('t', type=str, help='input file type')
args = parser.parse_args()


with gzip.open(args.i, 'r') as seq_file:
    with open(args.o, 'w') as headers:
        for record in Bio.SeqIO.parse(seq_file, args.t):
            headers.write(record.id)


#usage:
#gets headers from zipped sequence file

# ./get_headers.py multifasta.fa output.txt fasta
