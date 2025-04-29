
## InsCLR: Improving Instance Retrieval with Self-Supervision
Zelu Deng, Yujie Zhong, Sheng Guo, Weilin Huang
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/19930 - InsCLR: Improving Instance Retrieval with Self-Supervision.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share the link to their implementation (https://github.com/zeludeng/insclr). There are instructions on downloading the data, instructions on how to run the training procedure and how to change the configuration. The code is almost without comments, which makes the code slightly harder to follow but it is not an extremely large repository. The authors provide details on the archticture and training details in the implementation details section.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors provide a table of data sets with download links in their implementation documentation. The authors provide citation on the training data with some statistics in the paper. Four public benchmark datasets are named and cited but no other information is provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide full configuration files in their implementation documentation. The authors state in the caption of table 3 that results were acquired with 'careful hyper-parameter tuning' but no explanation what the strategy/method of that was. No details on the hyperparameters are mentioned in the paper.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors specify the training procedure and data. Other data sets are used for testing. Results seem to indicate single runs, can be easily checked against their implementation. The metrics are not explained. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires decent experience with self supervision to understand the method and the experiments conducted.
