
## Contrastive Representation for Data Filtering in Cross-Domain Offline Reinforcement Learning
Xiaoyu Wen, Chenjia Bai, Kang Xu, Xudong Yu, Yang Zhang, Xuelong Li, Zhen Wang
Keywords: 
ICML/2024/Proceedings/32951 - Contrastive Representation for Data Filtering in Cross-Domain Offline Reinforcement Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/BattleWen/IGDF). In the readme they introduce the method with an image, describe the tasks and datasets with a download link, instructions on how to run the code, a few notes on the environments. The code needs more comments and the directory structure an index. Algorithm 1 provides pseudo code on their method and figure 3 is the same as the one in the readme. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

There authors provide a direct download link in their implementation. The authors state they use three environments from a public library which is included in the implementation installation. The authors state some modifications regarding the simulators which they publish. The environments are not described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors summarise all HP values in table 7 of appendix D.2. However the authors method (algorithm 1) is parameter free (except that it takes in aparametrised policy which are specified in that table). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors average over 5 runs and compute the normalised average score over 10 episodes. The metric is environment (data/task) related. Data split not applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise in RL cross-domain.
