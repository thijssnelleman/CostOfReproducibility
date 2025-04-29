
## Neuron Dependency Graphs: A Causal Abstraction of Neural Networks
Yaojie Hu, Jin Tian
Keywords: 
ICML/2022/Proceedings/17975 - Neuron Dependency Graphs: A Causal Abstraction of Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The implementation is available online (https://github.com/phimachine/ndg). In the readme they introduce the method, provide installation instructions, and an introduction on how to run the code with some explanation on which scripts can be used for analysis. The code can use more comments. Pseudo code is available in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(5/5)

There are some automatic downloading scripts for the datasets in the implementation, but not all. They list the datasets used in table 1 and 2 with some statistics on each. No citations given on the datasets or descriptions. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors describe the architecture per dataset in table 1. There seem to be some hardcoded hyperparameters in the implementation that are not mentioned in the paper. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The data sets have static train/test splits. The validation sets are either given or taken randomly 10% of the training set. The authors measure training and test accuracy. The results are single run/model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries experience with NN analysis (dependency graphs).
