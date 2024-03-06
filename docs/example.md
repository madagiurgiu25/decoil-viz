## Install

This image contains all the dependencies needed to run the software.
No additional installation needed.

```commandline
git clone https://github.com/madagiurgiu25/decoil-viz.git
cd decoil-viz
```

To download the docker image:

```
# for docker
./install.sh --docker
```

To download the singularity image:

```
# for singularity
./install.sh --singularity
```

## Run test example on your machine

0. Check installation

```
decoil-viz --version
```

1. Download test files from [zenodo:10679429](https://zenodo.org/records/10679429)

```commandline
# create example folder
mkdir -p $PWD/example
chmod 777 $PWD/example

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

2. Run test example

With docker

```commandline
bash test_docker.sh
```

With singularity

```commandline
bash test_singularity.sh
```

3. Check your output

The run test with create an `example` directory in your `$PWD` and show have the following structure:

```
example/
├── reconstruct
│   ├── 18.pdf
│   ├── 9.pdf
│   └── all_ecdna_elements.pdf
├── reconstruct.html

```

And the output is:

- `reconstruct.html` - Report with all reconstruction threads
- `reconstruct` - Folder containing the invididual reconstruction threads as .pdf for publication purpose


4. Description of the input

- `coverage.bw` - Coverage file in .bw format inferred from the original .bam
- `reconstruct.ecDNA.filtered.bed` - Reconstruction regions file in .bed like format
- `reconstruct.ecDNA.filtered.links.txt` - Reconstruction links file in .txt format
- `summary.txt` - Reconstructions summary	
- `gencode.v42.primary_assembly.basic.annotation.gtf` - Genes annotation file 
- `GRCh38.primary_assembly.genome.fa` - Reference genome

For more details about how these files are generated go to [decoil](https://github.com/madagiurgiu25/decoil-pre)

