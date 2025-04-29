
## A Markov Framework for Learning and Reasoning About Strategies in Professional Soccer
Maaike Van Roy, Pieter Robberechts, Wen-Chi Yang, Luc De Raedt, Jesse Davis
Keywords: 
JAIR/2023/Proceedings/13934 - A Markov Framework for Learning and Reasoning About Strategies in Professional Soccer.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

Although the authors do not provide their implementation, the author state various packages and frameworks used in the footnotes, with version numbers, filling in a lot of questions for the independent investigators. An overview is missing however, like an illustration, which would have helped even more.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors state the datasets used in 7.1 with a high level stastitical overview in table 1. There is no citation, but in footnote 7 the authors link a library that does the automatic downloading of these datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors conduct 5-fold cross-validation on the training set to tune HPs, detailed in appendix A.1. They samples 50 parameter settings and state the distributions in A.1. and those not included 'were set to their default values'. They do not state the selected values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The data is split into 70-30 training/testing. The authors use AUROC and Brier to evaluate, presenting average + std. They also present log pointwise predictive density averaged with std error. Population is all 20 considered teams. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on MDP and sports data.
