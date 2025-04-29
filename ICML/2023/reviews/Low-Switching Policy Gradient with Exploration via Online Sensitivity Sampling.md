
## Low-Switching Policy Gradient with Exploration via Online Sensitivity Sampling
Yunfan Li, Yiran Wang, Yu Cheng, Lin Yang
Keywords: 
ICML/2023/Proceedings/24206 - Low-Switching Policy Gradient with Exploration via Online Sensitivity Sampling.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors provide pseudo code on their method in algorithm 1 with a practical version in algorithm 2. In the appendix they provide 5 other pieces of pseudo code. The authors describe a few details regarding the practical implementation of their method in 5.1. The authors state the package they developed their method in in appendix G.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use simulators from a public source which they cite. They use three environments but do not describe them. No direct link is available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors summarise the hyperparameters and their values in appendix G per method. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The results are averaged over 5 runs of random seeds, presented with standard deviation. The metrics are 'performance', it seems to suggest environmental reward but this is not actually stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in RL policies.
