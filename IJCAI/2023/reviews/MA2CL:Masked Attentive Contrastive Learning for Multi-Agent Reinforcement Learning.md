
## MA2CL:Masked Attentive Contrastive Learning for Multi-Agent Reinforcement Learning
Haolin Song, Mingxiao Feng, Wengang Zhou, Houqiang Li
Keywords: Machine Learning: ML: Deep reinforcement learning, Agent-based and Multi-agent Systems: MAS: Coordination and cooperation, Machine Learning: ML: Representation learning
IJCAI/2023/Proceedings/0470 - MA2CL:Masked Attentive Contrastive Learning for Multi-Agent Reinforcement Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share a link to their implementation. They do present pseudo code in algorithm 1, and two framework/process schematics in figure 1,2. No practical details on the implementation are shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three benchmark simulated environments for their experiments. They provide citations on these, and descriptions in 5.1. As the implementation documentation are missing, no direct link is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors state in section 4 one hyperparameter as fixed to 1. In algorithm 1 they state many different parameters, and in section 5 they state 'other hyperparamters settings can be found in supplementary materials'. These are not present nor linked. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use episode reward as metrics, a simulation env based value. They state in sec 5 the agent number is equal to 1. The authors state 5 random seeds were used for each experiment and that they present the mean and std dev.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries experience with RL and MAS.
