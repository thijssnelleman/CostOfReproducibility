
## Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning
Boyin Liu, Zhiqiang Pu, Yi Pan, Jianqiang Yi, Yanyan Liang, D. Zhang
Keywords: 
ICML/2023/Proceedings/25199 - Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/liuboyin/LAIES). In the readme they state installation instructions and how to run the code with various examples. The repository structure is large and could use an index. The code could use some more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use simulated environments which are installed through the implementation. They are cited in the paper. The environments are explained in appendix A2/3, and there are a few details available and their configurations in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyperparameter values they introduce in appendix A per experiment but not very structured. No explanation regarding the acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure the win rate of agents over six random seeds per scenario. The aggregation and variance is not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in RL.
