
## Not All Tokens Are What You Need for Pretraining
Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, yelong shen, Ruochen Xu, Chen Lin, Yujiu Yang, Jian Jiao, Nan Duan, Weizhu Chen
Keywords: 
Award: Best Paper Runner-up
NeurIPS/2024/Proceedings/457 - Not All Tokens Are What You Need for Pretraining.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

In figure 2 and 4 the authors visualise the method. The authors link two repositories used for evaluation. The implementation is not shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/3)

The authors discuss the data set up in 3.1 where they state they create their own data set by blending two datasets and use two other open source data sets. Although their own data set is created from public data sets this result is not shared. Direct link to openhermes is given in the references. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The hyperparameter values are stated informally in 2.1. per setting. The acquisition is not specified. A full overview of the values is not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The dataset splits are stated in 3.1. The evaluation details are given in appendix E for the metrics with extensive citations. Figure 5 is pretraining results, table 2 show the effect of their pretraining, and in the pretraining corpus / pretraining setting some splits are given but a full overview of training/testing sets is not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries a lot of practical expertise on NLP and LLMS.
