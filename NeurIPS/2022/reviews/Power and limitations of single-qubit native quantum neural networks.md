
## Power and limitations of single-qubit native quantum neural networks
Zhan Yu, Hongshun Yao, Mujin Li, Xin Wang
Keywords: 
NeurIPS/2022/Proceedings/53390 - Power and limitations of single-qubit native quantum neural networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

Overview given in figure 1, frameworks specified in section 5. The authors provide their implementation in the supplementary materials (https://openreview.net/attachment?id=XNjCGDr8N-W&name=supplementary_material). In the readme they state installation requirements, an overview on the code files. The code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors model functions in their experiments (synthetic data). These functions are given in sec 5. Generators present in the code. Parameter values given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values are stated in section 5 in text. They are also present in the code (hardcoded). Acquisition is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors fit their models to functions (synthetic data). They present the results as plotted functions and in figure 6 they use MSE to present the training loss. No data split applicable

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on QNNs/
