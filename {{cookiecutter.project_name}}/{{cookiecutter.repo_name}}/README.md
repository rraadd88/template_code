# `{{cookiecutter.repo_name}}`

Source code

## Requirements  
1. python 3  
2. Anaconda package distributor   

## Usage

### Installing dependencies

Required python packages can be installed from the `yaml` environment file located in root directory of the repo.

    conda env create -f environment.yml

### Installing the package

    git clone https://github.com/{{cookiecutter.author_username}}/{{cookiecutter.repo_name}}.git;cd {{cookiecutter.repo_name}};pip install -e .
    
### Description of the scripts (located in [`{{cookiecutter.repo_name}}`](./{{cookiecutter.repo_name}}))

| script                                                              | description                                     |
|---------------------------------------------------------------------|-------------------------------------------------|
| [analysis00_numbers.py](./{{cookiecutter.repo_name}}/analysis00_numbers.py)     | analysis with the counts           |
| [analysis01_.py](./{{cookiecutter.repo_name}}/analysis01_.py)                   | some analysis |
| [curate.py](./{{cookiecutter.repo_name}}/curate.py)                             | wraper to curation scrispts                     |
| [curate01_.py](./{{cookiecutter.repo_name}}/curate01_.py)     | curation of some data                 |
| [curatemeta_annot.py](./{{cookiecutter.repo_name}}/curate03_annot.py)             | annotation of the datasets                      |
| [curatemeta_merge.py](./{{cookiecutter.repo_name}}/curate04_merge.py)             | merging of the datasets                         |
| [global_vars.py](./{{cookiecutter.repo_name}}/global_vars.py)                   | global variables of the analysis                |
| [plots.py](./{{cookiecutter.repo_name}}/plots.py)                               | plots                                    |
| [plot.zip](./{{cookiecutter.repo_name}}/plot.zip)                               | plots data                                    |
| [figures.ipynb](./{{cookiecutter.repo_name}}/figures.ipynb)                               | figures.ipynb                                    |
