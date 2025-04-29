
## Prompt Learning for Generalized Vehicle Routing
Fei Liu, Xi Lin, Weiduo Liao, Zhenkun Wang, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan
Keywords: Search: S: Search and machine learning, Machine Learning: ML: Applications, Search: S: Combinatorial search and optimisation
IJCAI/2024/Proceedings/0771 - Prompt Learning for Generalized Vehicle Routing.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/FeiLiu36/PromptVRP). Here the authors introduce the method with a visualisation and briefly explain: Directory structure, training procedure execution and testing execution. A lot of the code is very well documented with comments. The authors hard code the parameters into the execution script but they are grouped. The data and pretrained models are directly shipped with the code. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors include data and pretrained models in their implementation documentation. They state the instance generation procedure by referring to previous work and the appendix (which is not present, could have been included in the implementation docs), they also use two public real world data sets and provide the links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the model settings in 4.1, and can easily be checked against the implementation documentation. The authors do not state how these values are acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the training procedure in details in 4.1, how the training results were averaged in 4.2. The metrics are seemingly not explained and will require some expertise to understand. In 4.3 they state how the test results were acquired.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise in RL, the problem/task and how the instances are generated and zero-shot learning.
