import os, sys, re
from scipy import stats
if len(sys.argv) != 2:
    print("Usage: <script> <inroot>")
    exit()

inroot = sys.argv[1]

k = re.compile("\s+")

outfile = open ("/wtmp/user002/Comparative_genome/9_PositiveSelec/PositiveSelective_New2/Pvalue.txt", "w")
head = "gene\tlnL1\tlnL0\tDlnL\tp_value\n"
outfile.write(head)
    
for genefile in os.listdir(inroot):
        genefile_path = os.path.join(inroot, genefile)
        result_path = os.path.join(genefile_path, "result.txt")
        null_path = os.path.join(genefile_path, "result_null.txt")
        with open(result_path, "r") as infile:
            f1 = infile.read()
            info = "Bayes Empirical Bayes (BEB) analysis (Yang, Wong & Nielsen 2005. Mol. Biol. Evol. 22:1107-1118)\nPositive sites for foreground lineages Prob(w>1):"
            if info not in f1:
                continue
            else:
                list1 = f1.split(info)
                list2 = list1[1].split("The")
                if "*" not in list2[0]:
                    continue
        with open (result_path, "r") as infile1:
            for line1 in infile1:
                if line1.startswith("lnL"):
                    lnL1 = float(k.split(line1)[4])
        with open(null_path, "r") as infile2:
            for line2 in infile2:
                if line2.startswith("lnL"):
                    lnL0 = float(k.split(line2)[4])
        if lnL1 != 0 and lnL0 != 0:
            DlnL = 2 * (lnL1 - lnL0)
            p = (stats.chi2.sf(DlnL, 1))/2
            if p < 0.05:
                outline = genefile + "\t" + str(lnL1) + "\t" + str(lnL0) + "\t" + str(DlnL) + "\t" + str(p)+ "\n"
                outfile.write(outline)
outfile.close()
