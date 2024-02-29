#!/bin/bash
#
#SBATCH --partition=long
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=50G

singularity pull decoil-viz.sif  docker://madagiurgiu25/decoil-viz:1.0.3

