
## Improving physics-informed neural networks with meta-learned optimization
Alex Bihlo
Keywords: 
JMLR/2024/Proceedings/230356 - Improving physics-informed neural networks with meta-learned optimization.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 1 (https://github.com/abihlo/LearnableOptimizationPinns). The readme is empty. There are no installation notes except for installation of a single lib in the notebooks. The code has okay comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

They use synthetic simulation and introduce each per subsection in 5. Code is available in the notebooks. Parameters given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state they employed hyperparameter tuning to determine N, K and learning rate (values given) but do not state how this was done. Other parameter values can be found in the notebooks. Summarised in table 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

20 tasks are sampled per problem and train for 50 epochs. Results are presented over loss and optimiser updates, results are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise in meta-learning and optimisation.
