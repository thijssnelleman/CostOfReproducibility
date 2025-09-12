
## Sampling in Constrained Domains with Orthogonal-Space Variational Gradient Descent
Ruqi Zhang, Qiang Liu, Xin Tong
Keywords: 
NeurIPS/2022/Proceedings/53704 - Sampling in Constrained Domains with Orthogonal-Space Variational Gradient Descent.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in section 6 (https://github.com/ruqizhang/o-gradient). In the readme they mainly state which entry points to run for what experiment but its all very brief. No installation instructions. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use a synthetic distribution, the Adult Income dataset and Loan Classification (no citation on this dataset). The synthetic dist is explained clearly and sampled for n = 50. The adult dataset is included in the implementation as well as the loan (after a bit of digging as its named 'preprocessed.csv'). Synthetic generator included in implementation. Statistics not given on the datasets but tasks are explained. The authors also use CIFAR-10 and ImageNet which are not cited, included or described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

Hyperparameter stated in algorithm 1. This is not mentioned after. Default values can be found in the code, but it would have to be assumed that these were actually used for the presented experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

For figure 3 and 4 the authors measure logloss, logic loss, fairness loss, test accuracy, test violation and disparate impact. For table 1 they measure test error, expected calibration error (not explained) and AUROC. In table 1 they train on CIFAR-10 and use ImageNet as OOD test set. Most of the metrics are not described only cited. Data set splits for loan and income not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on orthogonal-space gradient flow.
