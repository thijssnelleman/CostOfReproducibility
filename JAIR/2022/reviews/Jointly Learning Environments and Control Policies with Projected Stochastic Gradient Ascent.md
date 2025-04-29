
## Jointly Learning Environments and Control Policies with Projected Stochastic Gradient Ascent
Adrien Bolland, Ioannis Boukas, Mathias Berger, Damien Ernst
Keywords: 
JAIR/2022/Proceedings/13350 - Jointly Learning Environments and Control Policies with Projected Stochastic Gradient Ascent.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in section 5 footnote 1 (https://github.com/adrienBolland/Jointly-Learning-Environments-and-Control-Policies-with-Projected-Stochastic-Gradient-Ascent). In the readme they describe the organisation of the code, how to install and how to run experiments with parameter explanation (brief). Code can use more comments. High level pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a Mass-Spring-Dampoer environment and describe it in 5.2. and appendix D. Parameter values provided. Implementation given in the repository.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values described in 5.2. There are also structured config files available regarding the experiments in the implementation. Acquisition not specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate expected return (env / RL standard), and present the results averaged with standard deviation and presented over iterations. Presented over 10 runs. Table 1/2 state the final values. Requires some expertise to understand figure 2.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries a solid experience base in RL and SGA.
