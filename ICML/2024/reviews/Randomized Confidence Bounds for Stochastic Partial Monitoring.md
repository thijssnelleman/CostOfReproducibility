
## Randomized Confidence Bounds for Stochastic Partial Monitoring
Maxime Heuillet, Ola Ahmad, Audrey Durand
Keywords: 
ICML/2024/Proceedings/32731 - Randomized Confidence Bounds for Stochastic Partial Monitoring.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share their implementation online (https://github.com/MaxHeuillet/partial-monitoring-algos). The code is a bit unstructured (including files) and could use more comments. Installation instructions and examples are provided for running the code.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two games to evaluate their method, for which they provide multiple citations, explain the actions / outcomes and extensively define them in appendix B. The code for these games are given in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors details their paramter space in appendix A through pseudo code with notes. The hyperparameter values are explored in appendix E. However the actually used values in section 5.1 and 5.2. are unclear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use regret as a metric (equation 1) and win-count of games. The results are accumulated over 96 experiments. No train/test split applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on game theory and algorithmics and their complexity. 
