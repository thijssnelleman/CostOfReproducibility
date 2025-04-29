
## Convergence Guarantees for the DeepWalk Embedding on Block Models
Christopher Harker, Aditya Bhaskara
Keywords: 
ICML/2024/Proceedings/32686 - Convergence Guarantees for the DeepWalk Embedding on Block Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors mainly present a theoretical work, however there is also an experimental section (4) in the paper. Especially the experiment in 4.2. means that it still applies. Thus: There is no implementation shared. The authors provide pseudo code in algorithm 1. There is a footnote 1 with some information regarding the implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/1)

The authors use synthetic data, share the details on how this is generated in section 4. The code of this is not shared. The parameters are clarified.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the configuration for their method in each experiments (4.1 and 4.2) which is clear based on algorithm 1. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

No train/test split applicable. The experiment is analysis on their methods behaviour. Data is single run. Metric is a formula which is clarified in the paper. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on optimisation algorithms / gradient descent, the deepwalk algorithm, geometrical deep learning and stochastic block models. 
