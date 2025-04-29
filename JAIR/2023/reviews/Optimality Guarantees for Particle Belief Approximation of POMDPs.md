
## Optimality Guarantees for Particle Belief Approximation of POMDPs
Michael H. Lim, Tyler J. Becker, Mykel J. Kochenderfer, Claire J. Tomlin, Zachary N. Sunberg
Keywords: 
JAIR/2023/Proceedings/14525 - Optimality Guarantees for Particle Belief Approximation of POMDPs.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors present a link to their implemention in section 6 (https://github.com/WhiffleFish/PFTExperiments). In the readme they show results and state how to run the code for reproducing experimental results. Code can use more comments, no installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use environments for their experiments, Laser Tag from DESPOT and Light Dark, VDP tag and Sub Hunt from POMPD. Each environment is well described and cited, and is available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors present the HP values in appendix F, where they provide a large table with all parameters and their value per algorithm and experiment combination. Acquisition not specified in the paper. There is a hyperopt statement in the implementation but this does not seem to help.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate reward per environment over particle count and present mean rewards  with two standard error.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on particle belief and POMDPs.
