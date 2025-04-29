## GOCPT: Generalized Online Canonical Polyadic Tensor Factorization and Completion
Chaoqi Yang, Cheng Qian, Jimeng Sun
Keywords: Data Mining: Mining Spatial and/or Temporal Data, Constraint Satisfaction and Optimization: Solvers and Tools, Data Mining: Mining Data Streams, Machine Learning: Online Learning
IJCAI/2022/Proceedings/0326 - GOCPT: Generalized Online Canonical Polyadic Tensor Factorization and Completion.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present their implementation online (https://github.com/ycq091044/GOCPT). The git repository is pip-installable which installs the requirements. There are instructions on how to run the code in various use-cases. The code has some comments and a reasonable amount of files (8) so it is easy to navigate. The files have meaningful names. There are no instructions on how to download the datasets.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4] 

There is a link to only three dataset in the datasets.py file (out of six used). Only one dataset in described. Statistics are provided. One dataset is private and the collection strategy is vaguely described. The authors used random perturbations to the data and provided code in the datasets.py file, the process is clearly described in the paper.

### Configuration
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors do not provide details on hyperparameters or tuning. There are default values for the hyperparameters in the code however it is unclear if these were used in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors clearly describe the metrics used. There is no need for train test split as there is no training phase. The method is deterministic and therefore does not require repetitions. Results aggregation is mean and standard deviations.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The field is highly-specialised, including the metrics used. It would therefore require some preparations to reproduce the paper. As one dataset is private, it is impossible to fully reproduce the results for it. For the rest, it is possible with reasonable effort.