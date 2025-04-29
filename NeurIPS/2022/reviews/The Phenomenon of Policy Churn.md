
## The Phenomenon of Policy Churn
Tom Schaul, Andre Barreto, John Quan, Georg Ostrovski
Keywords: 
NeurIPS/2022/Proceedings/54098 - The Phenomenon of Policy Churn.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors do no share their implementation. In the checklist they state this is because of proprietary code. The authors do state in the appendix the framework and many libraries it was implemented with. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use atari games environment and is cited in the appendix. There are some descriptions available but they are not very detailed.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Hyperparameters are given in appendix B.2 table 2 and stated they were taken from source methods (The authors benchmark/analyse other works in their paper).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Experiments are over 100 seeds and variance interquartile range and three seeds over 5 games. Metrics are policy change and convergence steps (training / objective related). Aggregation is sum or they give boxplots so not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise with RL theory.
