
## Unbiased Gradient Boosting Decision Tree with Unbiased Feature Importance
Zheyu Zhang, Tianping Zhang, Jian Li
Keywords: Machine Learning: ML: Applications, Machine Learning: ML: Classification
IJCAI/2023/Proceedings/0515 - Unbiased Gradient Boosting Decision Tree with Unbiased Feature Importance.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation (https://github.com/ZheyuAqaZhang/UnbiasedGBM). The readme has some instructions which are a bit difficult to follow. The code has very few comments, which complicates how easy it is to understand. The data is included in the repository. The repository itself is rather small, so although some reverse engineering will have to be done for re-implementation, its impact is limited.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(60/60)

The authors state they collect 60 datasets from Kaggle (open source). The authors state they give more details on it in Appendix C which is not present. One data set is included in the implementation docs. The lack of this appendix means we do not know exactly which datasets were used. The description of the data set collection however does make it possible for independent investigators to defend that their experiments are similar but to a certain limit.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state they tune the hyperparameters for 100 iterations on 60 data sets using optuna which they cite. They refer for details to the appendix which is missing. It is unclear which hyperparameters were optimised and will take quite some effort to determine from the code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state their metrics in 6.2 which they briefly introduce and produce citations on. They evaluate these metrics over iterations of tuning over the various models, which they evaluate on the test set and they seem to indicate in 5.2 that the splits are equally divided for t/v/t but this is not clear. It could also be that the data sets are already split. They show the methods averaged across the datasets, and state the shading indicates the variance.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires some understanding of ML classification.
