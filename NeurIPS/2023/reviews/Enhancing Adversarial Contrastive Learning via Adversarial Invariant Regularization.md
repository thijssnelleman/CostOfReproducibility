
## Enhancing Adversarial Contrastive Learning via Adversarial Invariant Regularization
Xilie Xu, Jingfeng ZHANG, Feng Liu, Masashi Sugiyama, Mohan Kankanhalli
Keywords: 
NeurIPS/2023/Proceedings/69867 - Enhancing Adversarial Contrastive Learning via Adversarial Invariant Regularization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/GodXuxilie/Enhancing_ACL_via_AIR). In the readme they state installation requirements, scripts on how to run pretraining with various examples and how to finetune. The code has okay comments. Structure is overseeable. High level overview in figure 1, pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use CIFAR-10, CIFAR-100 and STL as datasets. Downloaders included in the code. Citations given but no statistics or descriptions.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state hyperparameters delta 1 and 2 in their pseudo code but as well as learning rate, batch size and budget epsilon and epochs E. The delta values are stated in sec 4 as 0.5, batch size 512, epsilon as 8/255 and LR 5.0 with a cosine annealing schedule. An ablation analysis (grid search) is done on the delta parameters in appendix C.2. and they state they use this to determine the values used. For all other parameters acquisition is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use test accuracy (two types), and they report the mean over 15 types of corruption. They evaluate over various levels of corrpution and specify the parameters. Data split not specified for test set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on adversarial learning.
