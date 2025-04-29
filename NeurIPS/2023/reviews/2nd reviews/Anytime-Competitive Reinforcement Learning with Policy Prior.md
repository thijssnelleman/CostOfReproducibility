## Anytime-Competitive Reinforcement Learning with Policy Prior
Jianyi Yang, Pengfei Li, Tongxin Li, Adam Wierman, Shaolei Ren
Keywords: 
NeurIPS/2023/Proceedings/72273 - Anytime-Competitive Reinforcement Learning with Policy Prior.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

There is no code provided, nor are there any implementation specific details such as libraries or language used. The method is described in two pseudo-algorithms, but only on a very high level.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

There is only one task environment used, which is cited. The procedure and goal of the environment is described in the appendices, as well as the parameter settings. The simulation is based on dataset that are also cited. I do give some point as obtaining and combining all elements necessary to come to as simulation seems difficult. For example, there is a vague mention of augmenting the dataset to 400 episode, but what that exactly entails is left out.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The hyperparameters of the methods and their values are fully specified in the appendices, but only in text. Nothing is mentioned about how those settings were obtained.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The metrics used to evaluate the methods are clearly explained in the paper. What part of the data is used for training and testing is specified in the appendices. However, They remain a bit vague on how the results are actually obtained and no mention of repetitions is present, nor is there always a measure of variance provided.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

In general, this paper touches mostly on the field of RL, so the required background knowledge is limited. Based on the paper, the method should be reasonably well to reproduce if you have experience with building RL algorithms. However, reproducing the simulation environment requires reading additional literature that is cited in this paper. The paper is also quite math heavy and understanding the definitions and proofs requires a higher degree of mathematical understanding. However, I do not think understanding all the proofs and definitions is necessary to reproduce the results.
