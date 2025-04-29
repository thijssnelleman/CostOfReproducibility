
## Progressive Ensemble Distillation: Building Ensembles for Efficient Inference
Don Dennis, Abhishek Shetty, Anish Prasad Sevekari, Kazuhito Koishida, Virginia Smith
Keywords: 
NeurIPS/2023/Proceedings/70061 - Progressive Ensemble Distillation: Building Ensembles for Efficient Inference.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide a link to their implementation (https://github.com/metastableB/bdistil). The repository is (literally) empty. The authors state in appendix D the framework used. Pseudo code is given in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(8/8)

The authors use simulated data and six real world datasets. The two simulators are described in 5.1. but implementation is missing. In appendix C.1. more details are given and statistics on the datasets. Direct links and descriptions missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values are specified in appendix C.2. and model architecture parameters in table 2,3,4,5,6 and 7. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate accuracy vs inference time in figure 2, averaging the ensemble with error bars. Train test split is given in appendix C.1. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on ensembling.
