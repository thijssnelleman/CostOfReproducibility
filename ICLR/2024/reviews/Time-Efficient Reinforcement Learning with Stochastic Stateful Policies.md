## Time-Efficient Reinforcement Learning with Stochastic Stateful Policies
Firas Al-Hafez, Guoping Zhao, Jan Peters, Davide Tateo
Keywords: 
ICLR/2024/Proceedings/19415 - Time-Efficient Reinforcement Learning with Stochastic Stateful Policies.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide an implementation link in the abstract (https://github.com/robfiras/s2pg). Readme has an overview of the method, how to install, brief details on how to run experiments. Code has good comments. Structure needs an index. Pseudo code in appendix C.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

Authors use environments from MuJoCo Gym: AtlasPOMDP-Carry, HumanoidPOMDP-Walk, HumanoidPOMDP-Run. Download instructions in repo. Few details provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

HPs not discussed but can be extracted from code (with some effort). 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Results show the mean and 95% confidence interval, over 10 seeds. Data split n/a. metric is environment reward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

n/a
