
## Disentangling Domain and General Representations for Time Series Classification
Youmin Chen, Xinyu Yan, Yang Yang, Jianfeng Zhang, Jing Zhang, Lujia Pan, Juren Li
Keywords: Machine Learning: ML: Time series and data streams, Machine Learning: ML: Classification, Machine Learning: ML: Deep learning architectures
IJCAI/2024/Proceedings/0424 - Disentangling Domain and General Representations for Time Series Classification.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/IJCAI-CADT/cadt). Here they provide an appendix with implementation details and pseudo code, a readme with dependency/installation instructions, a short overview of the directory structure, and an instruction on how to run the code with a short explanations on the parameters. The code is largely without comments except for the data handler, which seems to also handle the fetching of the data sets.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors use five publicly available data sets, provide citations on them, and lengthy descriptions with statistics in the supplementary. The implementation documentation has data downloading built in to the code, from which the links can be easily extracted or use the code to do it.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

In the implementation details, the authors provide to run scripts in which configurations are set. In the appendix the authors conduct a hyperparameter analysis for two parameters (grid). For other hyperparameters their values are stated or can be determined from previous work which they cite. For a few parameters the acquisition is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

No details are given regarding training/testing split of the data in the paper, but could be extracted from the implementation with a bit of effort. The authors state they use accuracy as metric in table 1. It is not clearly specified what the variance is in table 1 nor what it is aggregated over.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires an understanding of time series data tasks.
