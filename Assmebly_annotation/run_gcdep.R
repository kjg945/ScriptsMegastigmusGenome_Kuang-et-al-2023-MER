args<-commandArgs(TRUE)

if(length(args) < 3 ) {
  stop("USAGE: run_gcdep.R  gc.table  depth.dable  out.pdf  min_gc  max_gc  min_dep max_dep \n")
} else{
  file1 = args[1]
  file2 = args[2]
  outpdf = args[3]
  mingc = as.numeric(args[4])
  maxgc = as.numeric(args[5])
  mindp = as.numeric(args[6])
  maxdp = as.numeric(args[7])
}

args[6]
args[7]
 
library(tidyverse)
gc <- read.table(file1, header = F , row.names = 1)
dp <- read.table(file2, header = F , row.names = 1 )

gc1 <- rownames_to_column(gc,var = "id")
dp1 <- rownames_to_column(dp,var = "id")

gcdep <- inner_join(gc1, dp1, by = "id")

colnames(gcdep) <- c("id", "gc", "dep")

p <- ggplot( data = gcdep )  + 
  geom_point(aes(x=gc,y=dep), colour = "red", alpha = 0.5 ,cex = 0.7) + 
  xlab("GC content")  + 
  ylab("Depth") +
  xlim(mingc, maxgc) +
  ylim(mindp, maxdp) +
  theme_bw()

ggsave(outpdf, plot=p)
  

