
## SeMAIL: Eliminating Distractors in Visual Imitation via Separated Models
Shenghua Wan, Yucen Wang, Minghao Shao, Ruying Chen, De-Chuan Zhan
Keywords: 
ICML/2023/Proceedings/23839 - SeMAIL: Eliminating Distractors in Visual Imitation via Separated Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

Figure 2 provides an overview on the method. The authors provide a link to their implementation in appendix C (https://github.com/yixiaoshenghua/SeMAIL). In the readme the authors state installation instructions, how to train with various parameter settings and how to plot the training. They also acknowledge other repositories they used for their implementation. The code has very few comments. The structure is large and could use an index. There are details on the implementation in appendix C.4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(7/7)

The authors use simulated environments. The authors provide environment parameters in appendix C. They also use a subset of a dataset for which they provide a citation and brief description and place in the implementation. The environments are referenced as well and explained in the appendix. They are included in the implementation.


### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors summarise the hyperparameters in appendix C.4. A full summary of all considered HPs and acquisition strategy are not given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors provide training details in appendix C. The authors repeat each experiment over 4 seeds. They present them averaged over episodic returns (environment metric) but the variance is not very clearly specified ('range of performance').

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires experience iwth RL.
