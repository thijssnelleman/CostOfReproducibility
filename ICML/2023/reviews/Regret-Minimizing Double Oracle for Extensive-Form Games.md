
## Regret-Minimizing Double Oracle for Extensive-Form Games
Xiaohang Tang, Le Cong Dinh, Stephen Mcaleer, Yaodong Yang
Keywords: 
ICML/2023/Proceedings/24799 - Regret-Minimizing Double Oracle for Extensive-Form Games.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/xiaohangt/RMDO). In the readme they state installation instructions, how to run the experiments with various examples. The code can use more comments. Pseudo code is available in the paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use environment simulators from a public package, cite it, and is automatically installed in the implementation. The environments are described in length in appendix C. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors define a hyperparameter in algorithm 2. This parameter is evaluated on a grid in figure 1. Afterwards they conduct experiments with single values for this parameter which is given per experiment. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure exploitability as a metric (Formula defined in 2.1). The results are single runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in game theory, Nash Equilibirium and double oracles.
