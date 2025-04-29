
## Flexible Residual Binarization for Image Super-Resolution
Yulun Zhang, Haotong Qin, Zixiang Zhao, Xianglong Liu, Martin Danelljan, Fisher Yu
Keywords: 
ICML/2024/Proceedings/32619 - Flexible Residual Binarization for Image Super-Resolution.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. Some minor details are given, figure 4 shows high level overview and algorithm 1 pseudo code. The authors state the framework they use for the implementation in 4.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors use 6 public datasets, provide citations on each. No descriptions/statistics or direct links given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state various hyperparameter values in 4.1. However the pseudo code of algorithm 1 is (nearly) parameter free. As the model its applied on is less relevant (we care about the presented method).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the training and testing sets per dataset. The authors state the metrics used in 4.1 with citations but do not provide complete explanations. The results are single models. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on binarization. 
