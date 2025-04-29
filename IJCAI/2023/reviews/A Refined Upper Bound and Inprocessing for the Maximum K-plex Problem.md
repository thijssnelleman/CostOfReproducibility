
## A Refined Upper Bound and Inprocessing for the Maximum K-plex Problem
Hua Jiang, Fusheng Xu, Zhifei Zheng, Bowen Wang, Wei Zhou
Keywords: Search: S: Combinatorial search and optimisation, Constraint Satisfaction and Optimization: CSO: Constraint optimization, Search: S: Heuristic search
IJCAI/2023/Proceedings/0623 - A Refined Upper Bound and Inprocessing for the Maximum K-plex Problem.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their implementation online (https://github.com/huajiang-ynu/ijcai23-kpx). The readme only states the purpose of the repository. The code readme has instruction on how to compile, how to run and example output. It also contains a data set called bio-yeast. The code has some comments, but not a lot. The authors also include the source of one of the baselines.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors include a dataset in their implementation documentations, which seems to be a subset of one of the data sets used for evaluation. The authors provide brief descriptions the three data sets and a direct link in their paper. A bit more information would be welcome in the paper on the data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Based on the implementation and the stated pseudo code, the method seems to be parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method on the data set, and state the cutoff time for each experiment. They evaluate the number of instances solved over various k values. The experiment is relatively straightforward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The methyod requires some expertise on the problem (Constraint optimisation) and algorithmic complexity.
