
## Two-stage Semi-supervised Speaker Recognition with Gated Label Learning
Xingmei Wang, Jiaxiang Meng, Kong Aik Lee, Boquan Li, Jinghan Liu
Keywords: Natural Language Processing: NLP: Speech, Machine Learning: ML: Semi-supervised learning
IJCAI/2024/Proceedings/0718 - Two-stage Semi-supervised Speaker Recognition with Gated Label Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state their code, data and models are published online (https://github.com/aitssgll/semi-supervised-speaker-recognition). However, the readme is nearly empty, and all code is written in one file. The code is parametrised, indicating configuration/hyperparameter options + default values. The code has some comments. The models and data are not found. The structure of the code, although one lengthy file, is a bit difficult to follow but should serve as a basis for re-implementation. In general the implementation can be improved with better documentation. A description on the implementation is given in 4.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors state the data is published in their implementation, but this is not found. A closer inspection of the code's arguments reveal some URLs. They state the sources of their data in 4.1 with citations, and provide short description on them.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors describe some hyperparameter values in 4.1 but it should be verified against the implementation if all needed values are specified. No acquisition strategy is specified. This could be lowered by providing config files for the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state the metric used, which is common in this field/task (rpiro knowledge). The authors state one of the data sets is collected as testing set, however the process is a bit obscure. The results seem to indicate single runs, but this requires some field expertise to verify.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires domain knowledge regarding semi-supervised learning.
