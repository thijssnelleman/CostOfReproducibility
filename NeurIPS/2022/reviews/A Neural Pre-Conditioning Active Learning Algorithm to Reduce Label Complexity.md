
## A Neural Pre-Conditioning Active Learning Algorithm to Reduce Label Complexity
Seo Taek Kong, Soomin Jeon, Dongbin Na, Jaewon Lee, Hong-Seok Lee, Kyu-Hwan Jung
Keywords: 
NeurIPS/2022/Proceedings/53506 - A Neural Pre-Conditioning Active Learning Algorithm to Reduce Label Complexity.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state the code is included on the checklist. This can not be found however (neither in supplementary materials). Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use CIFAR-10 and CIFAR-100. No details given on the data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The hyperparameters are discussed briefly in 5.1. where the parameter Q from alg. 1 is explicitly stated. No acquisition or structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

Performance is averaged over 3 trials. Results are reported as average accuracy + standard deviation. In figure 1 they measure IoU. Data split not clear nor what set is reported on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in active learning.
