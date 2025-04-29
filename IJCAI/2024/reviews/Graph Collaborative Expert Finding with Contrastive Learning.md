
## Graph Collaborative Expert Finding with Contrastive Learning
Qiyao Peng, Wenjun Wang, Hongtao Liu, Cuiying Huo, Minglai Shao
Keywords: Data Mining: DM: Mining graphs, Data Mining: DM: Mining text, web, social media, Data Mining: DM: Networks, Data Mining: DM: Recommender systems
IJCAI/2024/Proceedings/0253 - Graph Collaborative Expert Finding with Contrastive Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation, nor are practical details given. Figure 2 gives a general overview of the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The authors use 6 public data sets, where they provide a direct link to, describe the tasks and give statistics in table 2. They also state how the data is treated for their experiments. This makes the data very accesible and defendable/explainable in terms of comparability.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameters were tuned on the validation set in 4.1. Their values are stated afterwards, and although seemingly complete it could be difficult to verify that this is indeed the case. The authors do not state how these values were acquired, except that they were tuned. In 4.5 they explore two hyperparameter values and show the results in figure 6.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state each experiment is repeated five times and the averages are reported. The authors state each data set is partitioned in to tvt as 80-10-10, and eem to indicate this split is static. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries a good understanding of graph mining.
