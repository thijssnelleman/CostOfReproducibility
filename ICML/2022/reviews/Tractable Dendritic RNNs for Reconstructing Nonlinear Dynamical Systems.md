
## Tractable Dendritic RNNs for Reconstructing Nonlinear Dynamical Systems
Manuel Brenner, Florian Hess, Jonas M Mikhaeil, Leonard Bereska, Zahra Monfared, Po-Chen Kuo, Daniel Durstewitz
Keywords: 
ICML/2022/Proceedings/17351 - Tractable Dendritic RNNs for Reconstructing Nonlinear Dynamical Systems.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/DurstewitzLab/dendPLRNN). In the readme they introduce the method and provide a few notes on the implementation. In the subdirectories there are installation instructions and steps on how to reproduce the experiments from the paper. The code has a decent amount of comments. The repository structure is quite large and there are some file explanations in the readmes here and there but that does not cover the giant structure

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors state and discuss the benchmarks used with citations in 4.2 and in total use six 'models'. These data files are included in the implementation. Statistics are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameter settings in appendix 6 per dataset. They conducted a grid search for various parameters and their selected values are reported in table S1. Not all parameter were optimised and are just stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the performance measures in detail in 4.1. The authors report the mean with standard error of the mean as variance. The set dataset splits are discussed in 4.1. but not competely clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise in RNNs.
