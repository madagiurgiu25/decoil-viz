"""
Visualize the graph using networkx
"""
import os

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

import decoilviz

def report_circles_r(outfile, params):
	"""
	Generate report with all the information about the circles
	"""
	# Load the rmarkdown package
	rmarkdown = importr("rmarkdown")

	# Specify the RMarkdown file to render
	print(os.path.dirname(decoilviz.__file__))
	rmd_file = os.path.join(os.path.dirname(decoilviz.__file__), "template.Rmd")

	# Convert the Python dictionary to an R list
	r_list = robjects.ListVector(params)
	print(r_list)

	# Render the RMarkdown file to HTML
	rmarkdown.render(rmd_file, output_file=outfile, params=r_list, output_format="html_document", intermediates_dir=os.path.dirname(outfile), run_pandoc = False, clean = False)
