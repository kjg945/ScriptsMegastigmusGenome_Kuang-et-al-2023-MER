import re,sys,os
from Bio import SeqIO
if len(sys.argv) != 3:
    print("Usage: <script> <inroot> <outroot>")
    exit()

inroot = sys.argv[1]
outroot = sys.argv[2]

for i in os.listdir(inroot):
    inpath = os.path.join(inroot, i)
    outname = i.split(".")[0] 
    genefile = os.path.join(outroot, outname)
    os.mkdir(genefile)
    outpath = os.path.join(genefile, "input.nuc")
    outfile = open(outpath, "w")
    count = 0
    str1 = ""
    for seq_record in SeqIO.parse(inpath, "fasta"):
        item = str(seq_record.id)
        count += 1
        seq = str(seq_record.seq)
        seqlen = len(seq)
        str1 += item + " "*(30-len(item)) + seq + "\n"
    outfile.write(str(count)+ "\t" + str(seqlen)+ "\n\n") 
    outfile.write(str1)
    outfile.close()
    
