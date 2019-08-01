from rohan.global_imports import *

# paths to files
import yaml
cfgp=f"{dirname(realpath(__file__))}/cfg.yml"
cfg=yaml.load(open(cfgp,'r'))
cfg={k:f"{dirname(realpath(__file__))}/{cfg[k]}" for k in cfg}

cfg['cfgp']=cfgp

#annot file
if exists(cfg['dgene_annotp']):
    ## get annotations
    from rohan.dandage.io_dfs import get_colsubset2stats
    cfg['dgene_annot']=read_table(cfg['dgene_annotp'])
    cfg['dgene_annot_stats']=read_table(cfg['dgene_annot_statsp'])
    cfg['dgene_annot_stats']=set_index(cfg['dgene_annot_stats'],'gene subset')
    # sample sizes for the legends
    cfg['colgene_subset2classes']=cfg['dgene_annot_stats'].apply(lambda x: x.index,axis=0)[cfg['dgene_annot_stats'].apply(lambda x: ~pd.isnull(x),axis=0)].apply(lambda x: dropna(x),axis=0).to_dict()
    cfg['colgene_subset2classns']=cfg['dgene_annot_stats'][cfg['dgene_annot_stats'].apply(lambda x: ~pd.isnull(x),axis=0)].apply(lambda x: dropna(x),axis=0).to_dict()
    cfg['colgene_subset2classns']={k:[int(i) for i in cfg['colgene_subset2classns'][k]] for k in cfg['colgene_subset2classns']}

    cfg['colgene_subsetpre2colxys']={'subset1 or subset2': ['subset1', 'subset2', 'unclassified'],
                             }
    ##vars
    cfg['cols_gene_subset']=list(cfg['colgene_subset2classes'].keys())

    cfg['gene_subset2colors']={
    'subset1':'#FF2A2A',
    'subset2':'#2A7FFF',
    }    

    cfg['colgene_subset2classcolors']={k:[cfg['gene_subset2colors'][s] for s in cfg['colgene_subset2classes'][k]] for k in cfg['colgene_subset2classes']}

## datasets for merging
cfg['dn2label']={  'dataset','Somebody et al.',
                }


## data types
cfg['dataset types']=['type1','type2']


cfg['dataset_']=[]
cfg['dataset_2color']=dict(zip(cfg['dataset_'],['#FF00FF','#A9A9A9','#00FF00','#0000FF','#FF0000']))

cfg['dataset2cols']=ordereddict({
'dataset1': [ 
        'col1',
        ],
      })
cfg['dataset_cols']=[]
for k in cfg['dataset2cols']:
    cfg['dataset_cols']+=cfg['dataset2cols'][k]

## plotting
# https://cduvallet.github.io/posts/2018/03/boxplots-in-python
# boxprops = {'edgecolor': 'k', 'linewidth': 2, 'facecolor': 'w'}
# lineprops = {'color': 'k', 'linewidth': 2}
# cfg['boxplot_kwargs'] = dict({'boxprops': boxprops, 'medianprops': lineprops,
#                        'whiskerprops': lineprops, 'capprops': lineprops,
# #                        'width': 0.75
#                       },)

# for jup notebook
for k in cfg:
    globals()[k] = cfg[k]