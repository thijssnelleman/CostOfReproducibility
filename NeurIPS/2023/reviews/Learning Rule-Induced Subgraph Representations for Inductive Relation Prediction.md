
## Learning Rule-Induced Subgraph Representations for Inductive Relation Prediction
Tianyu Liu, Qitan Lv, Jie Wang, Shuling Yang, Hanzhu Chen
Keywords: 
NeurIPS/2023/Proceedings/71668 - Learning Rule-Induced Subgraph Representations for Inductive Relation Prediction.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their implementation online (https://github.com/smart-lty/REST). In the readme they describe the repo structure, how to install, how to train and reproduce results, and how to visualise them. Code can use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use WN18RR, FB15K-237, NELL-995 as benchmark datasets (cited). Data sets statistics given in appendix B table 5. No descriptions or direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors use grid search for the parameters and specify them in appendix C. The optimal values for each data set is given in the code, although this will take a bit of digging. Not every hyperparameter is optimised.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use Hits@10 as metrics and evaluate each experiment five times with random seeds and report the mean. The datasets have static splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on inductive relation prediction, goemetirc deeplearning.
