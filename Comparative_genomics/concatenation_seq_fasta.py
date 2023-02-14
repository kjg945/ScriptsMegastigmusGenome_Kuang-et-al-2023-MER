#!/usr/bin/env python
import sys, re, os
from Bio import SeqIO

if len(sys.argv) != 2:
    print("Usage: <Script> <in_root> <outfasta>")
    exit()

k = re.compile("\s+")

inroot = sys.argv[1]
outroot = sys.argv[2]

dic = {}

for i in sorted(os.listdir(inroot)):
    if i.endswith(".fas"):
        inpath = os.path.join(inroot, i)
        for seq_record in SeqIO.parse(inpath, "fasta"):
            name = str(seq_record.id)
            sequences = str(seq_record.seq)
            if name not in dic:
                dic[name] = ""
            dic[name] +=  sequences

with open(outroot, "w") as outfile:
    for name in sorted(dic):
        outfile.write(">%s\n" % name)
        outfile.write(dic[name] + "\n\n")
        

    
