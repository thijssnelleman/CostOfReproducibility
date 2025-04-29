
## Generalization Guarantees of Self-Training of Halfspaces under Label Noise Corruption
Lies Hadjadj, Massih-Reza Amini, Sana Louhichi
Keywords: Machine Learning: ML: Learning theory, Machine Learning: ML: Semi-supervised learning
IJCAI/2023/Proceedings/0420 - Generalization Guarantees of Self-Training of Halfspaces under Label Noise Corruption.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/Lies0zeta/Self-Training-of-Halfspaces). In the readme they introduce the paper and state the benchmark datasets used. The notebooks have little documentation, the code in the experiments/src directory are well commented on. There are some details on their implementation in section 6. The readme could have some more details/instructions on the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(10/10)

The authors present statistics of the datasets in table 1, provide a citation and short description on it in section 6, but direct links (in the implementation for example) are missing. It is implied that the data is public ('consider datasets from'), but this could have been stated more clearly. In the implementation they do clearly state benchmark data sets on a list of five. Since they cite the same citation for all, we assume all are public benchmarks.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state the required inputs of their method in algorithm 1. However many more hyperparameters seem to be present in the implementation. These values are not discussed and will have to be reverse engineered from the implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the data set split under experimental setup, and evaluation metrics and that this process was repeated randomly twenty times and they report the averages. In table 2 caption they state they also report the mean + standard deviation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise with noisy data and general machine learning training procedures.
