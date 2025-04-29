
## Shuffle Private Linear Contextual Bandits
Sayak Ray Chowdhury, Xingyu Zhou
Keywords: 
ICML/2022/Proceedings/16281 - Shuffle Private Linear Contextual Bandits.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/sayakrc/Differentially-Private-Bandits). In the readme they refer to the method. No installation instructions. The code has okay comments. Pseudo code available in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use synthetic data simulation for their experiments. The simulator environments are present in the code. The parameters are given in section 5.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The parameters are defined in algorithm 1. The batch size is specified in section 5. The delta parameter is defined as formulae in section 3. No acquisition for batch size given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors average the results over 50 randomly generated instances for 20k rounds. Metric is regret defined in the introduction. No data split applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on bandits. 
