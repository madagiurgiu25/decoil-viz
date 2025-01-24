#!/bin/bash
#
#SBATCH --partition=long
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=50G

# image version
VERSION="1.0.4"

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

DECOILVIZ=$PWD
export PATH=$PATH:$DECOILVIZ

# Check if the line is already present in ~/.decoil_profile
if ! grep -q "$DECOILVIZ" ~/.bashrc; then
    echo "export PATH=\$PATH:$DECOILVIZ" >> ~/.bashrc
    echo "Append export PATH=\$PATH:$DECOILVIZ to ~/.bashrc"
    source ~/.bashrc
fi

# Check if the line is already present in ~/.bashrc
#if [[ $(grep "source ~/.decoil_profile" ~/.bashrc | wc -c) == 0 ]]; then
#    # If not present, append the line to ~/.bashrc
#    echo "Append: source ~/.decoil_profile to ~/.bashrc"
#    echo "source ~/.decoil_profile" >> ~/.bashrc
#fi

#source ~/.decoil_profile

