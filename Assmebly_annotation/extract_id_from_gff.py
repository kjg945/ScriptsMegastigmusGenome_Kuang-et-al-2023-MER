import sys

Usage = 'python <extract_id_from_gff> <in_gff> <outfile>\n'
if len(sys.argv) != 3:
    print(Usage)
    sys.exit()

infile = sys.argv[1]
outfile = sys.argv[2]
dic = {}
mRNA_id = ''
CDS_id = ''
with open(outfile, "w") as o:
    with open(infile, "r") as f:
        for line in f:
            if line[0] != "#":
                line1 = line.split("\t")
                if line1[2] == "mRNA":
                    mRNA_id = line1[8].split(";")[0].split("=")[1]
                    print(mRNA_id)
                if line1[2] == "CDS":
                    CDS_id = line1[8].split(";")[0].split("=")[1]
                dic[mRNA_id] = CDS_id
        for key, value in dic.items():
            o.write(key + '\t' + value + '\n')

