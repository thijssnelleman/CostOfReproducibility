
## Non-Asymptotic Guarantees for Robust Statistical Learning under Infinite Variance Assumption
Lihu Xu, Fang Yao, Qiuran Yao, Huiming Zhang
Keywords: 
JMLR/2023/Proceedings/220034 - Non-Asymptotic Guarantees for Robust Statistical Learning under Infinite Variance Assumption.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state they use the PyTorch Framework in 5.2. No other details given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

The authors conduct simulation studies in 5.1 and state the simulation in 5.1.2 with parameters. No implementation given. In 5.2. they also conduct simulation and provide the functions with parameters. In 5.3 they use the Boston Housing Dataset and state where they downloaded it from and provide a few details on it. They also use MNIST and state a few details but no links/citations. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss tuning parameters in 5.1.2 and state they conduct grid search with 5-fold cross validation for parameter alpha and p and lot the grids and the resulting criterion value in figure 2. For the real world datasets they specify also hyperparameter optimisation but not for each possible parameters, some are simply stated but not explained.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use accuracy as a metric, defined with formula in 5.2. They present the average in table 4 over 100 replications with varying values of Beta. In table 2/3 they preset the l2 estimation error for logistic regression. Table 5 they measure MAE over the boston dataset and state the data split in 5.3.1. and that they present results on the test set. For MNIST they also define an accuracy function in eq. 32. and the data split and present results on the test set. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on robust DNNs.
