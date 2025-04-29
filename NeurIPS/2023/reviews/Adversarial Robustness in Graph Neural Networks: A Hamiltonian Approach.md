
## Adversarial Robustness in Graph Neural Networks: A Hamiltonian Approach
Kai Zhao, Qiyu Kang, Yang Song, Rui She, Sijie Wang, Wee Peng Tay
Keywords: 
NeurIPS/2023/Proceedings/69981 - Adversarial Robustness in Graph Neural Networks: A Hamiltonian Approach.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/zknus/NeurIPS-2023-HANG-Robustness). In the readme they state installation requirements, how to reproduce the results with exact commands, and reference three other sources they used for their implementation. The code can use more informative comments. There are alot of files thus an index is welcome too.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(7/7)

The authors use 7 benchmark datasets in their experiments. Each has a citation provided. Four are included in the code for automatic download, three direct links are missing. Dataset statistics are given in appendix C table 5 and 6. Detailed descriptions missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state HP T in appendix C.2. and set the value to 3. They also state the step size is fixed to 1. Full parameter values per experiment can be found in the implementation. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors report accuracy in their results, but aggregation/variation not specified. Dataset splits are given in 6.1. It is noted in the appendix some results are on the test set but this is not explicitly stated everywhere.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

REquries expertise on GNNs and adverarial attacks/robustness.
