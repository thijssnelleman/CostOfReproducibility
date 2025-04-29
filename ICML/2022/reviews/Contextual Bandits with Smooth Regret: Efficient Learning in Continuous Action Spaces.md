
## Contextual Bandits with Smooth Regret: Efficient Learning in Continuous Action Spaces
Yinglun Zhu, Paul Mineiro
Keywords: 
ICML/2022/Proceedings/16947 - Contextual Bandits with Smooth Regret: Efficient Learning in Continuous Action Spaces.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors publish their code online (https://github.com/pmineiro/smoothcb). In the readme they state a few notes linking their experiments of the paper. Both experiments have their own readme describing the data, linking the notebooks and how to run. They directly link the data sets. The code has few comments. There are no installation instructions. Pseudo code is given in algortihm 1-3. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

Direct links to the datasets can be found in the implementation per experiment. The data sets are cited and described with some statistics in 6.1, but very few details in 6.2. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state their hyperparameter settings in 6.1. and state their initial chosen values worked well enough that no tuning was done (empirical, budget=1). The values can easily be found and checked in the notebooks.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the loss and regret in the experiments, with 38% confidence and 95% CI for variation. The results are over a population 10^3 data samples. Train test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on bandits. 
