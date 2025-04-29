
## PreNAS: Preferred One-Shot Learning Towards Efficient Neural Architecture Search
Haibin Wang, Ce Ge, Hesen Chen, XIuyu Sun
Keywords: 
ICML/2023/Proceedings/24952 - PreNAS: Preferred One-Shot Learning Towards Efficient Neural Architecture Search.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/tinyvision/PreNAS). In the readme they provide an overview of the method, installation instructiosn, a link to download the data and how to prepare it for the code, how to run examples and download links to their models. The code has very few comments. The structure is large and can use an index. There are some details on the implementation in section 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(7/7)

There is a download instruction the the pre-training dataset in the repository. In section 4.4 the authors provide citations on the test sets which are public. No description/statistics or download links given for the test sets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values are detailed in section C of the appendix and more are provided in section 4.1. There are more summaries available in the implementation. No acquisition strategy given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method on 6 datasets as test sets. The esults are single model. The metric is not mentioned.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on one shot learning for neurel architecture search.
