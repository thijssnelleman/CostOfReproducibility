
## Effect-Invariant Mechanisms for Policy Generalization
Sorawit Saengkyongam, Niklas Pfister, Predrag Klasnja, Susan Murphy, Jonas Peters
Keywords: 
JMLR/2024/Proceedings/230802 - Effect-Invariant Mechanisms for Policy Generalization.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link for their implementation in section 6 (https://github.com/sorawitj/effect-invariance). In the readme they state which files are linked to which subsection of the experiments. There is also a link to a dataset. There are no installation instructions. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

In section 6.1. the authors use simulated data, state the parameters and the distributions/formulae. The generator is provided in the code. The authors provide a link to a datasets (HeartSteps) for section 6.2/6.3, provide a citation and description but no statistics. In 6.4. they do a simulated study on the data, specify how they agument the data and create a new dataset and provide code on it.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

It is not entirely clear what parameters belong to the method and which to the simulation and how they interplay.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

Metric is relative reward(formula given) and rejection rate (task specific). Variance is over sample size and 5% significance level. No data split applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on policy generation
