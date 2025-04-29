
## A Multilabel Classification Framework for Approximate Nearest Neighbor Search
Ville Hyvönen, Elias Jääsaari, Teemu Roos
Keywords: 
JMLR/2024/Proceedings/230286 - A Multilabel Classification Framework for Approximate Nearest Neighbor Search.pdf
Project URL: https://github.com/vioshyvo/JMLR2024

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a project URL on the JMLR website (https://github.com/vioshyvo/JMLR2024). In the readme they state how to download the datasets through a scripts, how to compute the labels, what dependencies to install/requirements and how to compile, hwow to train/evaluate, where to find the grids of HPs for each algorithm, the results, how to make plots and tables and how to run with slurm. The code needs more comments and the structure an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors provide a data downloader and label builder for the datasets. They provide MNIST, FMNIST, GIST, STL-10, Trevi, SIFT / SIFT query. The authors provide details on the datasets in appendix A. There are some high level statistics in table 3. Only Fashion, GIST, STL-10 and Trevi were used in the experiments. The descriptions are a bit lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide grids for each algorithm in the parameters directory per dataset. The tuning process is detailed in A.3. The optimal/selected values are not specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The data downloader in the implementation creates static train/validation/test splits. They measure precision vs recall and recall vs query time and in table 2 query times as seconds per 1000 queries. Reqsults are single run (pareto frontiers with optimal HPs). The results are stated to be over the test set in section 8.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries experience with multilabel classification and ANNS.
