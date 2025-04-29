
## Graph Diffusion Policy Optimization
Yijing Liu, Chao Du, Tianyu Pang, Chongxuan LI, Min Lin, Wei Chen
Keywords: 
NeurIPS/2024/Proceedings/96349 - Graph Diffusion Policy Optimization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/sail-sg/GDPO). In the readme they state how to install, where to find data and how to prepare it, where to find pretarained models and how to train with an explanation how to configure, how to run the toy experiment, how to finetune, with various examples, how to evaluate. The structure is huge and could use more comments and docs.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

There are automatic downloader for some datasets in the implementation as well as links to it in the readme. In 6.1. the authors state the datasets used (SBM, Planar) as wel as in 6.2 (ZINC250k and MOSES) and in 6.3 (Spectral MMD). All are described with some statistics and citations but very briefly.  ZINC and moses have direct links in the implemtation, Planar and sbm will download automatically, spectral is not specified.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters are stated in A.1. Structured overview per experiment are given in files in the implementation. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The metrics are described per section. The data splits regarding train test are used of the original datasets. Aggregation/Variance is not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on RL and graph learning.
