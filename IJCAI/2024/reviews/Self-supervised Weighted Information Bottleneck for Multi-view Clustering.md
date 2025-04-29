
## Self-supervised Weighted Information Bottleneck for Multi-view Clustering
Zhengzheng Lou, Chaoyang Zhang, Hang Xue, Yangdong Ye, Qinglei Zhou, Shizhe Hu
Keywords: Machine Learning: ML: Multi-view learning, Machine Learning: ML: Clustering, Machine Learning: ML: Multi-modal learning, Machine Learning: ML: Unsupervised learning
IJCAI/2024/Proceedings/0513 - Self-supervised Weighted Information Bottleneck for Multi-view Clustering.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. They present a framework overview in figure 1 and pseudo code in algorithm 1. No details on the implementation are shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/6)

The authors share direct links to 4 out of 6 data set in the paper. Each data set has a short description with task explanation and some minor statistics. They provide more details in table 1. On the two large datasets its not clear if these are public as they are not linked nor cited, but are clearly described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the delta parameter in 3.3 was searched on a specified grid. The selected value for this is stated per data set. Based on algorithm 1, this is the only parameter for their method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used in 3.3. They state they conduct ten runs per experiment in 3.4, and in figure 6 they state the variance in the std, and in 3.4 they state they average. There are no details regarding train/test sets suggesting the whole data set was used for optimisation and results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on multi-view data and clustering.
