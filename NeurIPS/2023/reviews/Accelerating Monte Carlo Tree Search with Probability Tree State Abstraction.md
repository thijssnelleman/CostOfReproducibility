
## Accelerating Monte Carlo Tree Search with Probability Tree State Abstraction
Yangqing Fu, Ming Sun, Buqing Nie, Yue Gao
Keywords: 
NeurIPS/2023/Proceedings/73038 - Accelerating Monte Carlo Tree Search with Probability Tree State Abstraction.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/FYQ0919/PTSA-MCTS). In the readme they describe the method and provide a script to rerpoduce the examples. An installation file is present, the code needs more comments but the structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(8/8)

The authors use simulated environments which automatically install via implementation. No descriptions given at all.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

Hyperparameters are briefly stated in 5.3. The code reveals many more parameters. These are not discussed, but a starting point can be found in the code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors present the results with 10 seeds. Aggregation and variation not given. Train/test split not applicable. Metrics are environmental rewards.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on RL tasks and probability tree state abstraction.
