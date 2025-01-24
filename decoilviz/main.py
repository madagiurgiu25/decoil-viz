"""
Created using PyCharm
@author: Madalina Giurgiu
@date: 10:30 AM 02/01/24
"""

import argparse
import logging
import os
import sys
import traceback
import time
from pprint import pprint

import decoilviz
from decoilviz.utils import CONFIG_R as cr
from decoilviz.utils import ENV as env
from decoilviz import visualize

def run_plot_only(outputdir, 
                  sample, 
                  gtffile, 
                  refgenome,
                  bedfile,
                  linksfile,
                  bigwigfile,
                  summaryfile,
                  allowedchr="",
                  window="",
                  filterscore="", 
                  filtertop="",
                  suffix="reconstruct"):
	"""
	Run only reconstruction plot. Relies on the output internal structure
	"""
	permissions = 0o755
	outputdir = os.path.abspath(os.path.normpath(outputdir))
	os.makedirs(outputdir, exist_ok=True, mode=permissions)
	os.makedirs(os.path.join(outputdir,suffix), exist_ok=True, mode=permissions)

    # convert to absolute path
	bigwigfile = os.path.abspath(bigwigfile)
	bedfile_ecdna = os.path.abspath(bedfile)
	linksfile_ecdna = os.path.abspath(linksfile)
	summaryfile = os.path.abspath(summaryfile)
 
	refgenome = os.path.abspath(refgenome)
	gtffile = os.path.abspath(gtffile)
	genesfile =  cr.GENESANNO
	print("Genes file: ", genesfile)
 
    # change to local directory
	currpath = os.getcwd()
	os.chdir(outputdir)
	print("Current directory: ", os.getcwd())
    
	params = {cr.NODEFILE: bedfile_ecdna,
			  cr.EDGESFILE: linksfile_ecdna,
			  cr.SAMPLE: sample,
			  cr.BW: bigwigfile,
			  cr.MAXCOV: 100,
			  cr.REFGENOME: refgenome,
			  cr.GTFFILE: gtffile,
			  cr.GENESFILE: genesfile,
			  cr.DECOILVERSION: decoilviz.__version__,
			  cr.SUMMARYFILE: summaryfile,
			  cr.ROOT: os.path.normpath(outputdir) + "/",
			  cr.FNAME: suffix,
			  cr.WINDOW: window,
			  cr.FILTERSCORE: filterscore,
			  cr.FILTERTOP: filtertop,
              cr.EXTENDALLOWEDCHR: allowedchr
			  }
	visualize.report_circles_r(os.path.join(params[cr.ROOT], params[cr.FNAME] + ".html") , params)
	os.chdir(currpath)
	print("Current directory: ", os.getcwd())
 
def is_absolute_path(path):
    return os.path.isabs(path)

def validate_input(args):
    
    for i in [args.coverage, 
              args.summary,
              args.links,
              args.bed,
              args.outputdir,
              args.annotation_gtf,
              args.reference_genome,
              args.genes]:
        
        # check if path is absolute path
        if os.path.isabs(i) == False:
            raise ValueError("Path '{}' is not an absolute path. Please provide an absolute path.".format(i))
        
        # if this is a file check if exist
        if i not in [args.outputdir]:
            if os.path.exists(i) == False:
                raise ValueError("File '{}' is does not exist.".format(i))
            

def main(sysargs=sys.argv[1:]):
    
    parser = None
    args = None
    
    try:
        start_time = time.time()
        # parse arguments
        if len(sysargs) == 0:
            sysargs.append("--help")    
        
        parser = argparse.ArgumentParser(prog="decoil-viz",
                                            description="""Decoil-viz {}: visualize ecDNA reconstruction threads + report""".format(
                                            decoilviz.__version__),
                                            usage="decoil-viz --outputdir <outputdir> --name <sample> -r <reference-genome> -g <annotation-gtf> --coverage <bw> --summary <summary.txt> --bed <reconstruct.bed> --links <reconstruct.links.txt>")
        parser.add_argument('--version', action='version',
                            version='%(prog)s {}'.format(decoilviz.__version__))
        parser.add_argument('-o', '--outputdir', required=True, type=str)
        parser.add_argument('--name', help='Name of the sample', required=True)
        parser.add_argument('--coverage', help='Coverage file path', required=True)
        parser.add_argument('--bed', help='Bed file with reconstructions', required=True)
        parser.add_argument('--links', help='Links file with reconstructions', required=True)
        parser.add_argument('--summary', help='Summary of reconstructions', required=True)
        parser.add_argument('-r', '--reference-genome', help='Reference genome (fasta)', required=True)
        parser.add_argument('-g', '--annotation-gtf', help='GTF annotation', required=True)
        parser.add_argument('--suffix',help='Output suffix', required=False, default='reconstruct')
        parser.add_argument('--plot-top',
                            help='Keep only the top x reconstructions (default: %(default)d - denoting all)',
                            required=False, default=50, type=int)
        parser.add_argument('--plot-filter-score',
                            help='Keep reconstructions with estimated_proportions > x (default: %(default)d - denoting all)',
                            required=False, default=0, type=int)
        parser.add_argument('--plot-window',
                            help='Keep reconstructions within defined window (path to file in bed format)',
                            required=False, default="", type=str)
        parser.add_argument('--full', help='Generate full report', default=True, type=bool)
        parser.add_argument('--genes',help='Path to list of gene names / oncogenes', default="/code/anno/genes.txt", required=False)
        parser.add_argument('--extend-allowed-chr',help='Extend chromosomal annotation list (e.g. --extend-allowed-chr chr1,chr2)', default="", required=False)
        
        args = parser.parse_args(sysargs)

        # set path to gene list
        cr.GENESANNO = args.genes
        validate_input(args)
        os.makedirs(args.outputdir, exist_ok=True)
  
        run_plot_only(args.outputdir,
                    args.name,
                    args.annotation_gtf,
                    args.reference_genome,
                    bedfile=args.bed,
                    linksfile=args.links,
                    bigwigfile=args.coverage,
                    summaryfile=args.summary,
                    suffix=args.suffix,
                    window=args.plot_window,
                    allowedchr=args.extend_allowed_chr
                    # filterscore=args.plot_filter_score, 
                    # filtertop=args.plot_top,
                    )

        print("-------")
        print("Status: Successfully finished")
        print("User time (seconds): decoil-viz", round(time.time() - start_time, 2))
        print("Params:", args)
        print("#######")
        print()

    except AttributeError:
        parser.print_help()
        traceback.print_exc()
        
    except Exception:
        print("-------")
        print("Status: Failed")
        print("User time (seconds): decoil-viz", round(time.time() - start_time, 2))
        print("Params:", args)
        print("#######")
        print()
        traceback.print_exc()


if __name__ == '__main__':
	main()
