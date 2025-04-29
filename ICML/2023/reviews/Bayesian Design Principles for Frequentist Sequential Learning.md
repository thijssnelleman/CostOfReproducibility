
## Bayesian Design Principles for Frequentist Sequential Learning
Yunbei Xu, Assaf Zeevi
Keywords: 
Award: Outstanding Paper
ICML/2023/Proceedings/1082 - Bayesian Design Principles for Frequentist Sequential Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Pseudo code given. Implementation not found. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors use a simulated bernouulli multi armed bandits and state the procedure in 4.1 with parameter values per experiment. Implementation not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The η parameter is presented with various values, γ is fixed to 0.001. The latter choice is not explained. The choices of η is drawn from an interval [0.05,0.5] but its not stated with what strategy.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors average the results over 100 runs. The authors measur expected regret (defined in 2.2). Split not applicable. Aggregation is averaging. Variation not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on bayesian methods and multi-0armed bandits.
