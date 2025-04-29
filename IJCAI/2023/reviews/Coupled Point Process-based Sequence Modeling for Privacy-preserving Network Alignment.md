
## Coupled Point Process-based Sequence Modeling for Privacy-preserving Network Alignment
Dixin Luo, Haoran Cheng, Qingbin Li, Hongteng Xu
Keywords: AI for Good: Data Mining, AI for Good: Multidisciplinary Topics and Applications
IJCAI/2023/Proceedings/0678 - Coupled Point Process-based Sequence Modeling for Privacy-preserving Network Alignment.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/Dixin-Lab/CNPP). They provide installation details in the readme and three steps on how to run the code. Most of the code has a decent amount of comments. Pseudo code can be found in algorithm 1 and 2. Figure 1 gives a high level overview of the process. More details on the implementations are stated in 5.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors provide data in the implementation docs under synthetic data. They state in 5.1 they use 4 datasets, with a description and citation. The authors state statistics on the datasets in table 1. The authors do not provide direct links to the other datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors define hyperparameters in the pseudo code of algorithm 1 and 2. The authors state in 5.1 the values of most hyperparameters. They state 'for different datasets' they adjust the learning rate between two values, leaving it unclear what values were used and what type of search was conducted. They state for the three baselines they were optimised by grid search, but not what grids. This increases the effort to determine which set of HPs belongs to what experiment, and assess what budget was used. The authors do show the impact of variance in two parameters in table 4. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[9]

There are no statements regarding training/testing on the datasets, yet a training procedure is implied (since in 5.1 a learning rate per data set is mentioned). This makes it difficult to set up a similar experiment. There is also a variance in the results (table 2 for example), meaning the aggregatation and variance types are not given and we also do not know what type of population is created (folds over different data splits, different seeds, ...). The authors state the metric used and provide a citation on it + explanation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires some understanding of the graph tasks being conducted (network alignment), as well as privacy preservation, geometrical deep learning.
