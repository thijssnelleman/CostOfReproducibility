
## Direct Preference Optimization: Your Language Model is Secretly a Reward Model
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, Chelsea Finn
Keywords: 
Award: Outstanding Paper Runner-Up
NeurIPS/2023/Proceedings/42 - Direct Preference Optimization: Your Language Model is Secretly a Reward Model.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors share the code of their implementation in the supplementary material in appendix D. They state in which framework it was done. This gives a lot of practical details. High level overview in figure 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use IMDb dataset, Reddit TL;DR, and a human preference dataset. Citations are provided. No statistics, descriptions or direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the HP values in appendix B. The authors state 'virtually no tuning of hyperparameters' in the discussion. In sec 6.1. some grids are specified for the parameters. No tabular overview and optimisation strategy is a bit vague.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate win rate as a metric. In figure 3 results are over 22 runs with various configurations but the variation/ aggregation is unclear. They also conduct a human study which is fully detailed in appendix D.3. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on LLM evaluation and loss functions.
