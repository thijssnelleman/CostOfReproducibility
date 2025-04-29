
## FLS: A New Local Search Algorithm for K-means with Smaller Search Space
Junyu Huang, Qilong Feng, Ziyun Huang, Jinhui Xu, Jianxin Wang
Keywords: Machine Learning: Clustering, Search: Applications, Search: Combinatorial Search and Optimisation, Search: Heuristic Search, Search: Local search
IJCAI/2022/Proceedings/0429 - FLS: A New Local Search Algorithm for K-means with Smaller Search Space.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide extensive pseudo code, where algorithm 4 is their method which relies on the algorithms 1, 2 and 3 for parts of its execution. The authors do not share their implementation. No pratical details given. The amount of pseudo code is very extensive however, decreasing this cost.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

The authors summarise the datasets used with some statistics in table 1. They state in section 4 with a citations and direct link where this data can be found. The descriptions per dataset are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the algorithm configuration of their method in section 4. The parameter T varies per experiment. The parameters space is given in algorithm 4. No acquisition method / budget specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state each experiment is repeated 5 times and present the average results. The metrics are stated with a formula in the methodology paragraph (gap). Results are presented over the full data set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries experience in search algorithms and k-means.
