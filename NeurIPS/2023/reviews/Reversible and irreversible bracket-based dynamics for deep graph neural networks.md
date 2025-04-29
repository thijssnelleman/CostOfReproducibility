
## Reversible and irreversible bracket-based dynamics for deep graph neural networks
Anthony Gruber, Kookjin Lee, Nathaniel Trask
Keywords: 
NeurIPS/2023/Proceedings/72854 - Reversible and irreversible bracket-based dynamics for deep graph neural networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/natrask/BracketGraphs). They state in the readme the installation requirements. In the parameters.md they state the exact commands used for their experiments. The code has good comments. The structure is a bit strange and could use an explanation (src vs src-new for example). An overview is given in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(7/7)

The authors evaluate their method on four simulated environments and three benchmark datasets. Citations are provided on each. Direct links not given and the environments are not included in the implementation installation. Descriptions are given partially in the appendix but a bit lacking. Statistics on the datasets are given in B.3.1. table 7.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the exact commands used with parameter values in parameters.md of the implementation. For the environments, they state the HP values in text in appendix B.2.1 but this is a bit unstructured and some values are ambiguous. Acquisition not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors report results on the test set as average + std dev over 4/5/20 runs. Metrics are MAE, relative error and test accuracy. Data split strategies are provided. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on gemoetrical deep learning.
