install.packages("devtools", dep=TRUE,quietly = TRUE)
install.packages("ggplot2", dep=TRUE, quietly = TRUE)
install.packages("dplyr", dep=TRUE,quietly = TRUE)
install.packages("assertthat", dep=TRUE,quietly = TRUE)
install.packages("DT", dep=TRUE,quietly = TRUE)

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("GenomicRanges")
BiocManager::install("rtracklayer")
BiocManager::install('plyranges')

library(devtools)
Sys.setenv(R_REMOTES_NO_ERRORS_FROM_WARNINGS = TRUE)
devtools::install_github('mskilab/gUtils')
devtools::install_github('mskilab/fishHook', dependencies = TRUE)
devtools::install_github('mskilab/gTrack', dependencies = TRUE)
devtools::install_github('mskilab/gGnome', dependencies = TRUE)

