## TorchRL: A data-driven decision-making library for PyTorch
Albert Bou, Matteo Bettini, Sebastian Dittert, Vikash Kumar, Shagun Sodhani, Xiaomeng Yang, Gianni De Fabritiis, Vincent Moens
Keywords: 
ICLR/2024/Proceedings/18660 - TorchRL: A data-driven decision-making library for PyTorch.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to the implementation in the abstract (https://github.com/pytorch/rl). The readme has a list of updates/features/design principles, a link to a documentation website with various getting started examples, documentation links, installation instructions, and a link to a forum for questions. In general everything is extremely well documented.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(11/11)

HalfCheetah† Hopper† Walker2D† Ant† Pong‡ Freeway‡ Boxing‡ Breakout from Gym, navigation/balance/sampling from VMAS. Both cited, no descriptions.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authos benchmark previous work by reproducing them in their framework. They provide the used values in the appendix table 6-10 per method/environment. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

5 runs with different seeds and report the mean final reward and std and report the mean and standard deviation reward over 6 random seeds. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
