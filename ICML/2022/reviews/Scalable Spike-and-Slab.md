
## Scalable Spike-and-Slab
Niloy Biswas, Lester Mackey, Xiao-Li Meng
Keywords: 
ICML/2022/Proceedings/17225 - Scalable Spike-and-Slab.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors reference an R package and a link to a repository regarding their implementation (https://github.com/niloyb/ScaleSpikeSlab). We will only review the repository. In the readme they introduce the method, link the same package in R, and overview of the code. In the readme of the Python code they point to a tutorial which has okay documentation. The code files could use more comments. Pseudo code is in algorithm 2/3 of the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(8/10)

There is a dataset present in the code. The authors summarise the datasets used for their experiments in table 2 with some statistics. The datasets are fully described in appendix D with citations and direct links. Four datasets are indirectly linked through an R package. They state 2 are not publicly available but are well described however no acquisition strategy given. The synthetic datasets are not linked but the distributions and generation are explained. The generation code is not given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors describe the hyperparameter settings in appendix C, often refering to the previous works they use for their settings. Hyperparameters of their methods are described in section 1 and the pseudo code. Various values are stated per experiment but a full overview is missing. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate TPR, FPR and RMSE as metrics. They present the average + std dev over 20 indepent runs of the experiment. Each run generates their own dataset. In the appendix they conduct 10 fold cross validation. The data split for the other experiments is a bit unclear. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise in Gibbs sampling, bayesian regression.
