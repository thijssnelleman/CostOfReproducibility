
## Human Parity on CommonsenseQA: Augmenting Self-Attention with External Attention
Yichong Xu, Chenguang Zhu, Shuohang Wang, Siqi Sun, Hao Cheng, Xiaodong Liu, Jianfeng Gao, Pengcheng He, Michael Zeng, Xuedong Huang
Keywords: Knowledge Representation and Reasoning: Common-Sense Reasoning, Natural Language Processing: Question Answering, Knowledge Representation and Reasoning: Reasoning about Knowledge and Belief
IJCAI/2022/Proceedings/0383 - Human Parity on CommonsenseQA: Augmenting Self-Attention with External Attention.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state implementation details in section 3.1, but the actual implementation is not published. The authors do link a different repository to extract data. No other practical details are given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(17/17)

The authors state the 17 benchmark datasets used and summarise them in table 1. They state more details are included in the appendix but this is missing. They cite a source in 3.1. Direct link is not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in 3.1. A full summary on the hyperparameter space is not given. The authors state they selected various parameter values from a grid (budget is the grid size). The actual selected values are not clarified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state experiment with three different seeds and present the best (max aggregation) but not for each. The authors use accuracy as a metric. It is not clear how data is split into training/validation/test.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries experience in NLP and knowledge graphs.
