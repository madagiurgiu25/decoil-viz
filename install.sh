#!/bin/bash
#
#SBATCH --partition=long
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=50G

# image version
VERSION="1.0.3"

singularity_flag=false
docker_flag=false

# Function to print usage information
print_usage() {
    echo "Usage: ./install.sh [--docker|--singularity]"
}


# Parse command line arguments
while [[ $# -gt 0 ]]; do
     case $1 in
         --docker)
            docker_flag=true
	    shift 1
            ;;
        --singularity)
            singularity_flag=true
	    shift 1
            ;;
	*)
            echo "Unknown option: $1"
            print_usage
            exit 1
            ;;
    esac
done

if [ "$docker_flag" = true ]; then
	docker --version
	docker pull madagiurgiu25/decoil-viz:$VERSION
fi

if [ "$singularity_flag" = true ]; then
	singularity --version
	singularity pull decoil-viz.sif  docker://madagiurgiu25/decoil-viz:$VERSION	
fi

export PATH=$PWD:$PATH >> ~/.bashrc
