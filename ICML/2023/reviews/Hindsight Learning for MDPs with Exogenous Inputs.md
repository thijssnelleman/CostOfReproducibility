
## Hindsight Learning for MDPs with Exogenous Inputs
Sean R. Sinclair, Felipe Vieira Frujeri, Ching-An Cheng, Luke Marshall, Hugo Barbalho, Jingling Li, Jennifer Neville, Ishai Menache, Adith Swaminathan
Keywords: 
ICML/2023/Proceedings/24480 - Hindsight Learning for MDPs with Exogenous Inputs.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation online (https://github.com/seanrsinclair/hindsight-learning). In the readme they provide an overview of the code and state which code is missing due to being proprietary. Installation instructions are available per problem directory. A large part of the code seems to be copied from somewhere else and credit is only given in the paper. A lot of their own code seems to be without comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/3)

The authors consider three problems, two of which are available in their implementation. There they state the third is proprietary. The authors cite the source of one of the simulators, the source of one of the problems where they provide their own code to simulate, and for the proprietary they describe the problem in detail and cite another work for more details. The authors specify the settings of the simulators in each respective subsection. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the input for their method in algorithm 1. The authors state the hyperparameters tuned in appendix G table 6 (grid). However it is not fully clear which parameter setting was used for what experiment which should be extractable from the code base according to the authors.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure cummulative reward per method (environment). The variance is explained in the caption of table 1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise with MDP and RL.
