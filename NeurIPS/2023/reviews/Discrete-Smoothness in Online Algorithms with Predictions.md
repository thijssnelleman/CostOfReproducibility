
## Discrete-Smoothness in Online Algorithms with Predictions
Yossi Azar, Debmalya Panigrahi, Noam Touitou
Keywords: 
NeurIPS/2023/Proceedings/72382 - Discrete-Smoothness in Online Algorithms with Predictions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their code in the supplementary materials (https://openreview.net/attachment?id=DDmH3H78iJ&name=supplementary_material). There is no readme and few comments. No installation notes. Structure is small.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors generate input in sec 5. and state some parameter value alpha. The generation method is stated very briefly. The generator code is provided. The parameters vary per experiment and the values are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Based on the code and algorithms presented in the paper, the authors method is parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors present the results as mean + std dev in table 1. The data parameters are specified for each experiment. Its not clear what the population is table 1 aggregates over. Metric is competitive ratio which is explained in the introduction. Split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise in ml predictions and discrete smoothness for online algos.
