
## A Bayesian Bradley-Terry model to compare multiple ML algorithms on multiple data sets
Jacques Wainer
Keywords: 
JMLR/2023/Proceedings/220907 - A Bayesian Bradley-Terry model to compare multiple ML algorithms on multiple data sets.pdf
Project URL: https://github.com/jwainer/bbtcomp

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a repository link on the JMLR website and in section 8.1 with installation notes (https://github.com/jwainer/bbtcomp). They also provide some description and index on it in 8.1. In the readme they state more installation instructions, the data format with detailed explanations, certain set up steps, basic use examples and how to access the results + make plots, how to install the Python implementation and use it. The code has okay comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors evaluate a long list of datasets over a large set of baselines in section 5. They present 20 datasets in table 2. In total they discuss the evaluation of 128 datasets as can be found in the repository over 16 methods. It seems the authors do not actually use these datasets but rather the evaluations on these datasets of the method as input.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

There are various hyperparameters discussed in section 2, but not for the exploration in section 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results in table 4. The metrics are probabilities of the model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on bayesian models.
