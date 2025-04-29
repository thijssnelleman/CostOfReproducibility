
## Towards Hybrid-grained Feature Interaction Selection for Deep Sparse Network
Fuyuan Lyu, Xing Tang, Dugang Liu, Chen Ma, Weihong Luo, Liang Chen, xiuqiang He, Xue (Steve) Liu
Keywords: 
NeurIPS/2023/Proceedings/69975 - Towards Hybrid-grained Feature Interaction Selection for Deep Sparse Network.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation in footnote 1 (https://github.com/fuyuanlyu/OptFeature). In the readme they state how to do data preprocessing, how to run the code and a table of HP settings. No installation instructions. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors state they use three benchmarks, and provide direct links for two in the paper. The dataset statistics are given in appendix B table 3 and they preprocessing is described there too (scripts available in implementation). Descriptions on the datasets themselves are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

In 4.1 the authors state they tuned the HP values on grids (grid search) and specify them, they were tuned on the validation set. Selected values are given in the implementation (tabular format). Some parameters weren't tuned and are only stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method with AUC and Logloss as metrics. Results are reported with five different seeds and averaged. Results are on test sets but data split not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

REquries expertise on feature interaction selection.
