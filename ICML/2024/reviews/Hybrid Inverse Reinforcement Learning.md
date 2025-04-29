
## Hybrid Inverse Reinforcement Learning
Juntao Ren, Gokul Swamy, Steven Wu, J. Bagnell, Sanjiban Choudhury
Keywords: 
ICML/2024/Proceedings/35087 - Hybrid Inverse Reinforcement Learning.pdf
Project URL: https://github.com/jren03/garage

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/jren03/garage). In the readme they introduce the method, show the results, index the repository structure, describe how to install, how to autmatically download the used data, how to train and infer, how to reproduce plots from the paper, acknowlegdements for other implementations used to create theirs. The code has a decent amount of comments. Implementation details are also given in appendix B. Pseudo code is available in algorithm 2,3,4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors provide automatic data downloaders for 5 datasets in the implementation. These are actually environments which are provided publicly via MuJoCo lib (appendix B.1). The environment parameter delta value is provided in appendix table 1. The environments are not described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors specify the HPs in appendix B per experiment in table 2, 3, 4, 5, 6 and 7. No acquisition method specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they calculate standard error across 5 or 10 seeds per algorithm. The metrics are reward (environment). No train/test split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in RL.
