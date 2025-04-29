## Dimension Reduction and MARS
Yu Liu LIU, Degui Li, Yingcun Xia
Keywords: 
JMLR/2023/Proceedings/221422 - Dimension Reduction and MARS.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

There are no installation explanations, explanation of how to run functions but no working examples and unclear parameters. No datalinks () and no repository structure. (+1) There is an example script, but it is unclear whether this all what is needed for reproduciton. (+1) There are comments in the example script, but the rest is without comments. (+1)

### Data

_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]
  
(11/11)

They use four simulated dataset and seven real datasets. All simulated datasets have no direct link. All "real" datasets have direct links. All the real datasets have good description, the simulated do not. (0.73 points) hyperparameters for syntetic seems clear. Unclear whether code is available for simulators as only papers are cited, but code is available on github. 

### Configuration
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Authors provide table where different results for different parameters are summarised. the parameters are mentioned in the text as dimension and number which is non-descript.. +2, not clear how different values are chosen +1, budget unclear +1

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

1. Metrics very clearly explained by a formula. But elements of formula are not specified in the section where the metric is explained but somewhere else, 0.5 points?
2. clear that was evaluated on the testing data. and split is clear from the code.
3. I think it was performed 100 times and averaged so this is clear
4. 3

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

This paper is quite heavy on the mathematical proof side. It would take quite some time to thorougly understand all this. On the other side, the code is available which can function as a crutch. 
