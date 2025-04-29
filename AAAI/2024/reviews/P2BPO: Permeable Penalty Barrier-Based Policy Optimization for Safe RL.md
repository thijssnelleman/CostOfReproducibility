
## P2BPO: Permeable Penalty Barrier-Based Policy Optimization for Safe RL
Sumanta Dey, Pallab Dasgupta, Soumyajit Dey
Keywords: General
AAAI/2024/Proceedings/31928 - P2BPO: Permeable Penalty Barrier-Based Policy Optimization for Safe RL.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a source for their implementation (https://github.com/sumantasunny/P2BPO.git). However, the repository has a basically empty readme and the code is provided as a zip file which limits the accesibility. The authors also provide their appendix here. Upon downloading the zip and giving it a closer look, the authors provide (brief) instructions there regarding installation of the environment and running the training of the model.  They also state where what files will be placed. The documentation on the environments seems to belong to the gym library and was not written by the authors, but this is not clearly stated. There is another installation.md file which also does not seem to be written by the authors. Only the code in the safepo folder seems to belong to the authors, perhaps some was imported and modified but this is not clear. The safepo does contain well commented code and is nicely separating the configurations in yaml files.

In the paper the authors state they based it on another repository as base, which should also be stated in the implementation. The authors also provide pseudo code.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(8/8)

The authors use 8 publicly available benchmark environments and source code on them. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The method configuration files are available in the implementation documentation. The authors state algorihm specifc HP's will be the same across environments, but also environment specific params will be constant across all the algorithms. The authors state full HP definitions with default values in the appendix, and exact values used in all experiments. No description is given how these were achieved.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors clearly present the experiments training procedure for each environment/algorithm combination, and how they are tested. The metrics presented are briefly stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method requires a good understanding on reinforcement learning.
