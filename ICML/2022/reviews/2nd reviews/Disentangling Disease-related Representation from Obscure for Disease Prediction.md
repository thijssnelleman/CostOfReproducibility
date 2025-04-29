
## Disentangling Disease-related Representation from Obscure for Disease Prediction
Chu-ran Wang, Fei Gao, Fandong Zhang, Fangwei Zhong, Yizhou Yu, Yizhou Wang
Keywords: 
ICML/2022/Proceedings/17211 - Disentangling Disease-related Representation from Obscure for Disease Prediction.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

- The authors do not provide the implementation; cost increases by 4.
- The only info about implementation is that implement the models in PyTorch; cost increases by 3.
- There is no pseudocode, but there is a general figure of the proposed methodology, which is very clearly explained; cost increases by 1.
- There are some additional practical info about implementation (ResNet34 as encoder, Adam as optimiser), but not nearly enough to really help with reproducibility; no effect on cost.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/4)

- Only one dataset is public; there is a citation, but no direct link, cost increases by 1.
- There is no description of the datasets, cost increases by 1.
- There are statistics in the main paper and the appendix.
- The data is partially private, cost increases by 2.
- The authors refer to a previous study (Wang et al. 2021a) for the dataset settings they adopt. I didn't check the reference so I don't know how helpful it is. Cost increases by 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

- There are no details on hyperparameter optimisation at all; cost increases to the max.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

- There is info about metric (AUC-ROC which is quite standard), no impact on the cost.
- We see from the appendix that there is a train/valid/test split (but it is quite hidden), no impact on the cost.
- It is not clear how the split is performed, cost increases by 2.
- It is clear that the results are aggregated over 10 independent runs.
- In general, I feel like the presentation of the paper hinders a lot of info, and the level of English used to write the paper makes it quite hard to *disentangle* (hehe) what exactly is being done in terms of experimental protocol. Cost further increases by 1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The paper requires complete reimplementation of the method, which is conceptually relatively accessible, but technically tricky as one can only follow the textual description and formulas. The datasets are mostly private, but even if they were public, there is too much missing info to arrive to the state where you can meaningfully say that you can compare the reproduced conclusions with the original ones.
