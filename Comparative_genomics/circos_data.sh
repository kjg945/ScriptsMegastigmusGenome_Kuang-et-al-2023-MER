
## chromosome length
seqtk comp  genome.fasta |grep  "^LG" |awk '{print $1"\t"$2}' > genome.len

## chromosome file
awk '{print "chr\t-\t"$1"\t"$1"\t0\t"$2"\tchr"NR}' genome.len > Sind_karyotype.txt

## Generate window file with window size of 50Kb
bedtools  makewindows -w 50000 -g  genome.len > genome.window.bed

## Calculate the average GC content of each window
seqtk subseq genome.fasta  genome.window.bed  > genome.window.fasta
seqtk comp  genome.window.fasta |awk '{print $1 "\t" ($4+$5)/($3+$4+$5+$6) } ' |awk -F ":|-" '{print $1"\t"$2"\t"$3"\t"$4}'> Sind_gc.txt

## Calculate the number of genes in each window
bedtools intersect  -a genome.window.bed -b Sind.bed -c -F 0.1  > Sind_genecount.txt

## Calculate the repeat sequence proportion of each window
bedtools coverage -a  genome.window.bed -b  repeat.gff |awk '{print $1 "\t" $2 "\t" $3 "\t" $7}' > Sind_repeat.txt
