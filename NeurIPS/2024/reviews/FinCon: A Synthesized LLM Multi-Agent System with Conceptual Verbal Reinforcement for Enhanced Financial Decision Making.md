
## FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making
Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng Cao, Zhi Chen, Jordan Suchow, Zhenyu Cui, Rong Liu, Zhaozhuo Xu, Denghui Zhang, Koduvayur (Suba) Subbalakshmi, GUOJUN XIONG, Yueru He, Jimin Huang, Dong Li, Qianqian Xie
Keywords: 
NeurIPS/2024/Proceedings/94352 - FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors publish their code online and link it in footnote 1 (https://github.com/The-FinAI/FinCon). The repository is empty. Framework overview in figure 1 and 2. Pseudo code given in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[9]

(0/1)

In appendix A.5. the authors state the datasets collected and its sources, but few statistics or feature details are given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The hyperparameters in algorithm 1 are not really specified but there are variables that are not stated as input. Unclear what the hyperparameters are. There is a mention of a temperature variable being set to 0.3 in section 4.1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors train the method on one time period and evaluate on another (dates specified). The metrics are stated in sec 4.1. item 2 and appendix A.10. with formulae. The results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise in trading models and time series data as well as LLMs. Loads of practical experience required since the documentation regarding execution is very limited.
