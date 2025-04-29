
## Heterogeneous-Agent Reinforcement Learning
Yifan Zhong, Jakub Grudzien Kuba, Xidong Feng, Siyi Hu, Jiaming Ji, Yaodong Yang
Keywords: 
JMLR/2024/Proceedings/230488 - Heterogeneous-Agent Reinforcement Learning.pdf
Project URL: https://github.com/PKU-MARL/HARL

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors link their implementation on the JMLR website (https://github.com/PKU-MARL/HARL) and in footnote 1. In the readme they give an overview on the method, state how to install, provide links for environment installation, explain how to use the code, a table of algorithmic scopes, results and links to their source files. Code has okay comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors use simulated environments and provide installation instructions for them in the implementation. They in total use six (MPE, MAMuJOCO, SMAC, SMACv2, GRF and Bi-DexterouisHands), provide citations, visualisation in figure 4, and installation instructions for all. Descriptions could be better.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide configuration files for the algorithms in the implementation. They are also summarised in appendix K table 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25. The authors state they are set 'comparable' to baselines values (Which they take from previous works) for fairness.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure episode (environment specific) over steps. Results are presented over three random seeds, variation is standard deviation aggregation is median although this is not stated everywhere.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on RL.
