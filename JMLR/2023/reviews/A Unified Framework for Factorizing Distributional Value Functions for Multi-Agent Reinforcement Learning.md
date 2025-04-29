
## A Unified Framework for Factorizing Distributional Value Functions for Multi-Agent Reinforcement Learning
Wei-Fang Sun, Cheng-Kuang Lee, Simon See, Chun-Yi Lee
Keywords: 
JMLR/2023/Proceedings/220630 - A Unified Framework for Factorizing Distributional Value Functions for Multi-Agent Reinforcement Learning.pdf
Project URL: https://github.com/j3soon/dfac-extended

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website (https://github.com/j3soon/dfac-extended) and in section 6.4. In the readme they state extensions of the paper on the original work, link to a preview of the methods performance, installation instructions, a command for reproducing experiments with explanations on the arguments, how to compare with baselines, datails on how its updated, how to monitor running code and licenses. The structure is huge and really needs an index. Code comments look good in general.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use simulated environments in their experiments. They mainly use SMAC (citation provided) and describe what the task is. Links provided and is installed with the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss the HP values in 6.1. They select the hidden layer size from a grid, other values are fixed. In table 6 they show the selected hidden sizes for each method per environment task. They state the search is detailed in the supplementary material but this is not found. Config files can be found per algorithm. The details on acquisition are a bit lacking.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors reports the results over five independent runs. Metrics are win rate percentage and scores (environment reward, defined in sec 6). No data split applicable. Results are presented averaged, variance not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on RL.
