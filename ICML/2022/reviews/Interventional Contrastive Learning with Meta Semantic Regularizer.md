
## Interventional Contrastive Learning with Meta Semantic Regularizer
Wenwen Qiang, Jiangmeng Li, Changwen Zheng, Bing Su, Hui Xiong
Keywords: 
ICML/2022/Proceedings/17865 - Interventional Contrastive Learning with Meta Semantic Regularizer.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. In 6.2 they state a few implementation details regarding how the data was treated. In appendix A there is pseudo code on the method. In figure 3 there is a framework design.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(7/7)

The authors use 6 image benchmark sets, on which they provide citations and brief descriptions with a few statistics in 6.1. No direct links provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyperparameter values in 6.2. They evaluate the impact of some HPs in figure 5 and section 6.4. No overview or acquisition specified for the other HPs. There are many more HPs according to algorithm 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use top 1 and top 5 accuracy as metrics. A seperate dataset is used as test set. The results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in contrastive learning.
