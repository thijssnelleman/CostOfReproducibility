
## On the Importance of Feature Decorrelation for Unsupervised Representation Learning in Reinforcement Learning
Hojoon Lee, Koanho Lee, Dongyoon Hwang, Hyunho Lee, Byungkun Lee, Jaegul Choo
Keywords: 
ICML/2023/Proceedings/23546 - On the Importance of Feature Decorrelation for Unsupervised Representation Learning in Reinforcement Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/dojeon-ai/SimTPR). In the readme they state installation instructions, how to download the data and connect it to their implementation, how to run training code and finetuning with options. The code could use some more comments but its acceptable. The repository structure is large and can use an index. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use a benchmark which they cite and provide a very brief description on. No statistics given (except the 100k in the name). A data downloader is available in the implementation. The authors pretrain on a different dataset (DQN replay dataset) for which the same information is available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state various hyperparameter values in 4.1, and a full overview in appendix A table 5. and table 6. The authors frequently refer to it as the 'optimal setting'. No acquisition method specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the dataset splits in 4.1. The experiment results are repeated over 10 random seeds and reported with 95% CI over median/mean per metric which are all standard and defined over the problem.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on RL.
