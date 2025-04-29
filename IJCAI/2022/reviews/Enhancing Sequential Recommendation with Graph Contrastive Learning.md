
## Enhancing Sequential Recommendation with Graph Contrastive Learning
Yixin Zhang, Yong Liu, Yonghui Xu, Hao Xiong, Chenyi Lei, Wei He, Lizhen Cui, Chunyan Miao
Keywords: Data Mining: Recommender Systems, Machine Learning: Recommender Systems
IJCAI/2022/Proceedings/0333 - Enhancing Sequential Recommendation with Graph Contrastive Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not provide their implementation. They state their method was implemented using PyTorch. The framework in depicted in figure 2. No other practical details specified.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors state the statistics of the 4 datasets used in the experiments. They provide citations, how the data is selected/treated for their experiments. There are no descriptions or direct links for the data. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the parameter values in the implementation details. The authors conduct empirical and grid search on their hyperparameters but the selected values for each experiment is not specified. There is no full summary on all hyperparameters relevant to the method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the metrics used in 5.1 but no full explanation but are seemingly common in this field, how the data is split for validation and testing, how the metrics are aggregated over the output. The results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on recommender systems.
