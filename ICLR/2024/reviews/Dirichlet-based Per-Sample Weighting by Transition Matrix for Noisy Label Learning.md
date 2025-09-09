## Dirichlet-based Per-Sample Weighting by Transition Matrix for Noisy Label Learning
HeeSun Bae, Seungjae Shin, Byeonghu Na, Il-chul Moon
Keywords: 
ICLR/2024/Proceedings/19274 - Dirichlet-based Per-Sample Weighting by Transition Matrix for Noisy Label Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

Authors link their implementation in the abstract (https://github.com/BaeHeeSun/RENT). Readme has install info, how the dataset is generated and a link to another, performance overview. Seperate readme on how to run the code with parameter explanation but no examples. Code has few comments. Overview in fig 1 and pseudo code in alg 1.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

CIFAR10, CIFAR100, CIFAR10N, Clothing1M, all cited in 4.1. Too briefly described in F.1. Downloads through code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

Alpha grid search specified in footnote 5. Other HP detailed in text in F.1. No structured overview. Most values are not motivated.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

Authors report on test set with accuracy. Split not given. Agg/var not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
