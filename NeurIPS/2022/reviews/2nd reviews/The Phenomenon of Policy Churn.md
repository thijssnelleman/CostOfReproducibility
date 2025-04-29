## The Phenomenon of Policy Churn
Tom Schaul, Andre Barreto, John Quan, Georg Ostrovski
Keywords: 
NeurIPS/2022/Proceedings/54098 - The Phenomenon of Policy Churn.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

No code is provided. The used RL environments are mentioned and are well-known, but no implementation is readily available for all of them. The RL algorithms used are mentioned and references, however, no implementation is provided, which is crucial as performance commonly differs between implementations in RL.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

1/2

Both the Atari and the Catch environments are referenced, but no link is provided. The environments are only briefly described. All environment parameters are defined.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

All HPs of importance and their values are given in the paper, the rest is in the supplementary material. The parameters are set to match the original implementation of the methods used. Some variations of HPs are tried for the sake of an ablation study that is visualised in the paper

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The used performance criteria are either well-known within RL or well explained. It is clear how the evaluations are performed. The supplementary material provides details regarding the training settings and repetitions, but could be summarised better. For most results, a measure of variance is also provided and even boxplots are used.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Most of the work considers RL topics and RL researchers would not have many issues in understanding/reproducing this. This work is mostly an analysis of interesting behaviour in commonly known methods on commonly known environments.
