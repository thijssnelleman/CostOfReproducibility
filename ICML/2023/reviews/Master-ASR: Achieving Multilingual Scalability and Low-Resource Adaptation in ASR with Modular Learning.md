
## Master-ASR: Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning
Zhongzhi Yu, Yang Zhang, Kaizhi Qian, Cheng Wan, Yonggan Fu, Yongan Zhang, Yingyan (Celine) Lin
Keywords: 
ICML/2023/Proceedings/23475 - Master-ASR: Achieving Multilingual Scalability and Low-Resource Adaptation in ASR with Modular Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. Overviews are found in fig 1 and 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/2)

The authors use two datasets, one publicly available one which they describe with citation and another they collect themselves. They provide details on this data set in table 10. The collection strategy is not specified. No direct links or statistics given (except for very minor ones). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the parameter values in section 4.1. Their hyperparameter K is evaluated in an ablation study. A full overview of the HP space and values is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate accuracy per language in their experiments and also note the number of trainable parameters. The metric in table 2 and 3 is unclear. The train/test split is given per data set (static). Results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on multilinguag tasks and automatic speech recognition. 
