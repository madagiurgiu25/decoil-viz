#!/bin/bash
#
#SBATCH --partition=long
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=50G

ROOT=$PWD
REF=$ROOT/example/GRCh38.primary_assembly.genome.fa
GTF=$ROOT/example/gencode.v42.primary_assembly.basic.annotation.gtf
COVERAGE=$ROOT/example/coverage.bw
BED=$ROOT/example/reconstruct.ecDNA.filtered.bed
LINKS=$ROOT/example/reconstruct.links.ecDNA.filtered.txt
SUMMARY=$ROOT/example/summary.txt
OUTDIR=$ROOT/example
NAME=test

decoil-viz --singularity --coverage $COVERAGE --summary $SUMMARY --reference $REF --annotation-gtf $GTF --bed $BED --links $LINKS --outputdir $OUTDIR --name $NAME --extend-allowed-chr chrTest
