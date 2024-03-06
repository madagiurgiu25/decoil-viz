
## Run test example on your machine

0. Create output directory

```commandline
mkdir -p $PWD/example
chmod 777 $PWD/example
```

1. Download test files from [zenodo:10679429](https://zenodo.org/records/10679429)

```commandline
# configure variables
REFERENCE=$PWD/example/GRCh38.primary_assembly.genome.fa
GTF=$PWD/example/gencode.v42.primary_assembly.basic.annotation.gtf
COVERAGE=$PWD/example/coverage.bw
BED=$PWD/example/reconstruct.ecDNA.filtered.bed
LINKS=$PWD/example/reconstruct.links.ecDNA.filtered.txt
SUMMARY=$PWD/example/summary.txt
OUTDIR=$PWD/example
NAME=test

# download example data
wget -O - https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_44/GRCh38.primary_assembly.genome.fa.gz | gunzip -c > $REFERENCE
wget -O - https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_44/gencode.v44.primary_assembly.basic.annotation.gtf.gz | gunzip -c > $GTF
wget -O - https://zenodo.org/records/10679429/files/coverage.bw > $COVERAGE
wget -O - https://zenodo.org/records/10679429/files/reconstruct.ecDNA.filtered.bed > $BED
wget -O - https://zenodo.org/records/10679429/files/reconstruct.links.ecDNA.filtered.txt > $LINKS
wget -O - https://zenodo.org/records/10679429/files/summary.txt > $SUMMARY

# test your files exist
ls -lthr $REF
ls -lthr $ANNO
ls -lthr $COVERAGE
ls -lthr $BED
ls -lthr $LINKS
ls -lthr $SUMMARY
```

2. Run test example:

With docker

```commandline
bash test_docker.sh
```

With singularity

```commandline
bash test_singularity.sh
```

