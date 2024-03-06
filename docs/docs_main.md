
## Run decoil-viz directly with docker

Full usage of `madagiurgiu25/decoil-viz:1.0.3`.

```
docker run madagiurgiu25/decoil-viz:1.0.3 decoil-viz --help

usage: decoil-viz --outputdir <outputdir> --name <sample> -r <reference-genome> -g <annotation-gtf> --coverage <bw> --summary <summary.txt> --bed <reconstruct.bed> --links <reconstruct.links.txt>

Decoil-viz 1.0.1: visualize ecDNA reconstruction threads + report

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -o OUTPUTDIR, --outputdir OUTPUTDIR
  --name NAME           Name of the sample
  --coverage COVERAGE   Coverage file path
  --bed BED             Bed file with reconstructions
  --links LINKS         Links file with reconstructions
  --summary SUMMARY     Summary of reconstructions
  -r REFERENCE_GENOME, --reference-genome REFERENCE_GENOME
                        Reference genome (fasta)
  -g ANNOTATION_GTF, --annotation-gtf ANNOTATION_GTF
                        GTF annotation
  --suffix SUFFIX       Output suffix
  --plot-top PLOT_TOP   Keep only the top x reconstructions (default: 50 -
                        denoting all)
  --plot-filter-score PLOT_FILTER_SCORE
                        Keep reconstructions with estimated_proportions > x
                        (default: 0 - denoting all)
  --plot-window PLOT_WINDOW
                        Keep reconstructions within defined window (path to
                        file in bed format)
  --full FULL           Generate full report
```


