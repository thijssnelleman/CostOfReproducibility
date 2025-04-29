
## Efficient Structure-preserving Support Tensor Train Machine
Kirandeep Kour, Sergey Dolgov, Martin Stoll, Peter Benner
Keywords: 
JMLR/2023/Proceedings/201310 - Efficient Structure-preserving Support Tensor Train Machine.pdf
Project URL: https://github.com/mpimd-csc/Structure-preserving_STTM

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state their implementation link on the JMLR website and in footnote 1 in section 4 (https://github.com/mpimd-csc/Structure-preserving_STTM). In the readme they describe the method, structure of the repository, setup requirements, results and some results. The structure is massive and really needs an index so its +2 instead of +1. Comments are okay.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use four datasets, describe them in section 4.1 with citations and direct links, and also some files on them in the implementation. Statistics are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state parameter tuning in section 4. They consider three parameters R, sigma and C and specify the grids they are chosen from based on best classification accuracy over 5-fold cross validation. The selected values are not given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present their results over 20 runs on the test set measuring accuracy and presenting the average + 95% CI. Test set is given by k-fold cross validation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on SVM and kernel approximation.
