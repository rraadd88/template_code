from {{cookiecutter.repo_name}}.curate01_ import *
get_d_(test=False)

from {{cookiecutter.repo_name}}.curate03_annot import *
get_d_()

from {{cookiecutter.repo_name}}.curate04_merge import *
get_dmerge_agg_annot(test=True).head()
get_dmerge_lin(test=True).head()
get_dmerge_lin_annot(test=True).head()
