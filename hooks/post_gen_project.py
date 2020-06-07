from os.path import exists
import subprocess
## 1 make 2 analysis directories
subprocess.call("cookiecutter --no-input https://github.com/rraadd88/template_notebooks.git",shell=True)

dir2ps=['data_','data_annot','data_merge','figs','plot',]
for dir1p in dir2ps:
    subprocess.call(f"mkdir {{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}/{dir1p};ln -s {{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}/{dir1p} 00_something",shell=True)