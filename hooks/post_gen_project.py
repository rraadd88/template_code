from os.path import exists
import subprocess
## 1 make 2 analysis directories
subprocess.call("cookiecutter --no-input https://github.com/rraadd88/template_code_analysis.git",shell=True)

dir2ps=['data_merge','data_annot']
for dir1p in dir2ps:
    subprocess.call(f"ln -s {{cookiecutter.repo_name}}/{dir1p} 00_something",shell=True)