#! /usr/bin/env python3

##USAGE: ./rename_reads.py <path to your reads>


#script goes through zipped files in a directory and renames them using the following regex pattern used by QIIME2: '.+_.+_L[0-9][0-9][0-9]_R[12]_001\\.fastq\\.gz'

#assumes format: SampleName-Adapter-Adapter-L001-R[12]-001.fastq.gz

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, help='path to directory with the reads you want to rename')
args=parser.parse_args()

#scans through directory provided in argument
for entry in os.scandir(args.dir):
    # if the entry is a file
    if entry.is_file:
        print(entry.name, 'is a file') #debug
        if entry.name.endswith('gz'):
            os.chdir(args.dir)
            print(entry.name, 'is zipped') #debug
            file_name = entry.name
            #replace all dashes with underscores, this should be compatible with qiime regex matching
            new_name = file_name.replace('-','_')
            print("NEW NAME:", new_name) #debug
            #give the entry the new name created
            os.rename(entry.name, new_name)
            print('File has been renamed')
        else:
            print(entry.name, 'is NOT ZIPPED') #debug	
    else:
        print(entry.name, 'is NOT a file') #debug
    os.chdir(os.pardir)


