## Uncertainty-aware Constraint Inference in Inverse Constrained Reinforcement Learning
Sheng Xu, Guiliang Liu
Keywords: 
ICLR/2024/Proceedings/18968 - Uncertainty-aware Constraint Inference in Inverse Constrained Reinforcement Learning.pdf
Project URL: https://openreview.net/attachment?id=ILYjDvUM6U&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation link in the abstract (https://github.com/Jasonxu1225/Uncertainty-aware-Inverse-Constrained-Reinforcement-Learning). Readme has installation notes, how to run the code with examples. Structure is massive and needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(10/10)

The authors construct grid worlds, described in 6.1 and provide the code. Env details in appendix C. They also use 8 environments from Mujuco (installs with code) and HighD (same).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values per env in Table B.1. although discrete and highway are not included. However, config files per env can be found in the implementation. It will take a bit of effort to match them to the experiments. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use 4 random seeds, reporting mean and std dev over env reward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
