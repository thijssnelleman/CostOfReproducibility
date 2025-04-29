
## Variational Partial Group Convolutions for Input-Aware Partial Equivariance of Rotations and Color-Shifts
Hyunsu Kim, Ye Gon Kim, Hongseok Yang, Juho Lee
Keywords: 
ICML/2024/Proceedings/32678 - Variational Partial Group Convolutions for Input-Aware Partial Equivariance of Rotations and Color-Shifts.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/yegonkim/partial_equiv). The readme is mainly a list of execution instructions. There are is a requirements list regarding the installation in one of the subdirs. The code could do with more comments and the directory structure is rather large which could use an index. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors describe the used datasets with examples and statistics. No citations given. No direct links present and its unclear if the code can fix this automatically. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameter settings are detailed in appendix B table 4. Here the values per experiment can be found and the considered space. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The used metric is accuracy. The authors seem to imply the datasets have their own test sets which they use but this is not clarified. The variance in the result tables are not explained. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise in CV. 
