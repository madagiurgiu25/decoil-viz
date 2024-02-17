import setuptools
import subprocess
import decoilviz

def check_r_package(package_name):
    try:
        # Run Rscript command to check if the package is installed
        result = subprocess.run(['Rscript', '-e', f'library({package_name})'], capture_output=True, text=True)
        return result.returncode == 0  # If returncode is 0, the package is installed
    except Exception as e:
        print(f"Error checking R package {package_name}: {e}")
        return False
    

def check_r_dependencies():
    
    packages = ["ggplot2",
                "GenomicRanges",
                "rtracklayer",
                "plyranges",
                "Gviz",
                "gGnome",
                "gTrack"]
    
    for p in packages:
        if check_r_package(p):
            print("""{} is installed""".format(p))
        else:
            print("""{} is not installed""".format(p))
            
with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(name='decoilviz',
				 version=decoilviz.__version__,
				 author="Madalina Giurgiu",
				 author_email="giurgiumadalina25@gmail.com",
				 description="Visualize ecDNA reconstruction threads",
                 long_description=long_description,
				 long_description_content_type="text/markdown",
				 license='MIT',
				 entry_points={
					 'console_scripts': [
						 'decoil-viz = decoilviz.main:main'
					 ]
				 },
				 extra_require={
					 "build": [
						 # Define environment variables for the build process
						 "IN_CONTAINER=True",
					 ],
				 },
				 package_data={'': ['Snakefile', '*.json', 'envs/*.yaml', '*.Rmd', '*.gtf', '*.fa', '*.txt']},
				 # install_requires=required,
				 python_requires=">=3.7.0",
				 packages=setuptools.find_packages(),
				 include_package_data=True,
				 keywords=[],
				 zip_safe=False)
