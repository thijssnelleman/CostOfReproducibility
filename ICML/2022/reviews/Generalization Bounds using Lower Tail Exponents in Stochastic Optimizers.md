
## Generalization Bounds using Lower Tail Exponents in Stochastic Optimizers
Liam Hodgkinson, Umut Simsekli, Rajiv Khanna, Michael Mahoney
Keywords: 
ICML/2022/Proceedings/16195 - Generalization Bounds using Lower Tail Exponents in Stochastic Optimizers.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state in 4.1. that their method was developed in PyTorch. Implementation is not shared. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors state they use two data sets, both of which are public. No details or links/citations given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the various model architectures in section 4.1. Two parameters were evaluated from a grid. A full overview of the parameters is not given so its not clear if all information is available.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure PL exponent (Not explained) of each model on the datasets. The authors use standard splits given by the datasets. Each point on the graph is a single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise with stochastic optimisers.
