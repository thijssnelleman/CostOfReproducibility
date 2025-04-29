## STEM: Unleashing the Power of Embeddings for Multi-Task Recommendation
Liangcai Su, Junwei Pan, Ximei Wang, Xi Xiao, Shijie Quan, Xihua Chen, Jie Jiang
Keywords: DMKM: Recommender Systems, DMKM: Applications
AAAI/2024/Proceedings/29441 - STEM: Unleashing the Power of Embeddings for Multi-Task Recommendation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors present their implementation online (https://github.com/LiangcaiSu/STEM). The README file clearly states how to run the code, but only on one dataset. Instructions on how to run the code on other datasets are missing and it is unclear if running the same command works for other datasets as well. However, there are multiple files with no documentation on how to navigate through them. The files are missing comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use four datasets. All of them are public and have citation. However, the authors provide link to only one of them. There is also pre-processing script to only one of them. The authors do not describe the datasets but they do provide statistics.

### Configuration
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide the ranges of the values used in grid search, as well as some other constant hyperparameters. Although there is no table summarising the search space, I could easily find in the repository them in a summarised way. The authors provide hyperparameter values only for one dataset. The authors clearly state usage of grid-search for tuning.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors use well-known metrics (AUC and number of parameters in a neural network). The preprocessing script provided shows the train-val-test split for one dataset. However, for other datasets this information is missing. The authors do not provide details on multiple runs or CV and therefore also do not explain on an aggregation strategy.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Since the datasets pre-processing and download scripts are not provided, it requires some knowledge of the field of research, as well as some code-writing to create pre-processing as described in the paper. Understanding the results is not hard, as the metrics are commonly used in AI.