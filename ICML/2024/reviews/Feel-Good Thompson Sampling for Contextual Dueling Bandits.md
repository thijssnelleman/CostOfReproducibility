
## Feel-Good Thompson Sampling for Contextual Dueling Bandits
Xuheng Li, Heyang Zhao, Quanquan Gu
Keywords: 
ICML/2024/Proceedings/33221 - Feel-Good Thompson Sampling for Contextual Dueling Bandits.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. Pseudo code is given in algorithm 1. No practical details shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/1)

The authors evaluate their method on synthetic data. The authors state the generation of the data in section 8 with parameters. The implementation is not shared.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors define two hyperparameters in algorithm 1. The authors specify four values in 8.1 regarding a sub algorithm used for their metthod as well. These values are static through the experiments. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state each experiment is 10 independent runs. In 8.2 the authors state they averaged over 30 trials. The variance in figure 1 and 2 is not explained. Regret is a default metric. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on bandits, thompson sampling and RL.
