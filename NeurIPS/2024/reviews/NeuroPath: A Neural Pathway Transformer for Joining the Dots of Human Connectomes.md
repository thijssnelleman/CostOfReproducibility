
## NeuroPath: A Neural Pathway Transformer for Joining the Dots of Human Connectomes
Ziquan Wei, Tingting Dan, Jiaqi Ding, Guorong Wu
Keywords: 
NeurIPS/2024/Proceedings/96225 - NeuroPath: A Neural Pathway Transformer for Joining the Dots of Human Connectomes.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to the implementation in footnote 6 (https://github.com/chrisa142857/neuro_detour). In the readme they state which code file can be used for what, the available datasets and methods. There is a requirements file regarding the installation. The code has few comments. The structure is quite large, howevel as some of the code files have been indexed in the readme it should be doable. In figure 1 the authors show the structure of their method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors state in sec 4 they use four public datasets in their experiments (HCPA, UKB, ADNI and OASIS). Each is described in detail with citations. Data set statistics are given in table 9. No direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The model architectures are briefly described at the end of section 4. A full overview or summary on the hyperparameters is not given. Their values can possibly be extracted from the code (hard coded) but it would have to be an assumption that they are the values used in the experiments. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors apply 5-fold cross-validation for each dataset. The authors measure accuracy and F1 score as metrics. In table 3 they present average ranking per method/dataset from table 2 and 1. Aggregation and variation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on neural brain data tasks. 
