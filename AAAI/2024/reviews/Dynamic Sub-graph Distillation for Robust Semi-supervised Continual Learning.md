
## Dynamic Sub-graph Distillation for Robust Semi-supervised Continual Learning
Yan Fan, Yu Wang, Pengfei Zhu, Qinghua Hu
Keywords: ML: Life-Long and Continual Learning, ML: Semi-Supervised Learning
AAAI/2024/Proceedings/30041 - Dynamic Sub-graph Distillation for Robust Semi-supervised Continual Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide a Github link to their repository (https://github.com/fanyan0411/DSGD) with clear instructions on the implementation dependencies, details on the pre processing of datasets and instructions on running an experiment. The code base itself however seems extensive and has sometimes few, sometimes nearly no comments. This could complicate re-implementation. The authors do provide a visualisation of the method in their paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use three publicly available datasets, cite them, provide descriptions on them, and even have 'automatic download' available in their implementation source.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors present a grid search on the topology graph construction. They evaluate the impact on performance of parameter K. Other default values can seemingly be found in the implementation details per model. How these were found is unclear, no search method or budget specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors denote their evaluation metric, and specify data division regarding training/testing. The authors state they use "averaged incremental accuracy", but not if the experiments were repeated under some procedure, implying single run results. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

This method requires a good understanding on graph learning, semi supervised and continual learning. However the authors do provide a good introduction to these topics through their related work and methods section.
