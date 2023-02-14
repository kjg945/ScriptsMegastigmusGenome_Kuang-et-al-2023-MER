

k=16
genome=../00.data/genome.fasta
fq1=../00.data/SRR8689962_HiC_1.fastq.gz
fq2=../00.data/SRR8689962_HiC_2.fastq.gz

## 加载环境
export PATH=/pub/software/ALLHiC/scripts/:/pub/software/ALLHiC/bin/:$PATH

## 构建index
ln -s  $genome ./draft.asm.fasta
bwa index  draft.asm.fasta  
samtools faidx draft.asm.fasta  

## 比对
bwa aln -t 24 draft.asm.fasta $fq1 > sample_R1.sai  
bwa aln -t 24 draft.asm.fasta $fq2 > sample_R2.sai  
bwa sampe draft.asm.fasta sample_R1.sai sample_R2.sai $fq1 $fq2 > sample.bwa_aln.sam 

## 比对结果过滤 HINDIII: AAGCTT , MBOI: GATC
PreprocessSAMs.pl  sample.bwa_aln.sam draft.asm.fasta HINDIII
filterBAM_forHiC.pl  sample.bwa_aln.REduced.paired_only.bam sample.clean.sam
samtools view -bt  draft.asm.fasta.fai  sample.clean.sam > sample.clean.bam


## 划分contig成group
ALLHiC_partition -b sample.clean.bam -r draft.asm.fasta -e AAGCTT -k $k

## Extract CLM file and counts of restriction sites
allhic extract sample.clean.bam draft.asm.fasta --RE AAGCTT

## 排序和方向优化
for K in ` seq 1 $k `
do 
    allhic optimize sample.clean.counts_AAGCTT.*g${K}.txt sample.clean.clm
done

## 得到最终结果
ALLHiC_build draft.asm.fasta

## 绘制heatmap 图

seqkit   fx2tab -l -i  -n  groups.asm.fasta > len.txt
grep 'sample.clean.counts_AAGCTT' len.txt > chrn.list
ALLHiC_plot sample.clean.bam groups.agp chrn.list 50k pdf
