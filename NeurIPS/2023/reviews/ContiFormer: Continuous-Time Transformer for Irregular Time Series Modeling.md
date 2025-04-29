
## ContiFormer: Continuous-Time Transformer for Irregular Time Series Modeling
Yuqi Chen, Kan Ren, Yansen Wang, Yuchen Fang, Weiwei Sun, Dongsheng Li
Keywords: 
NeurIPS/2023/Proceedings/71304 - ContiFormer: Continuous-Time Transformer for Irregular Time Series Modeling.pdf
Project URL: https://seqml.github.io/contiformer/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their project page where a link to their implementation can be found (https://github.com/microsoft/SeqML/tree/main/ContiFormer). In the readme they state updates, refer for installation requirements to the parent repom, provide instructions to reproduce experiments, state how to download the datasets with links, scripts for hyperparameter search. The code can use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors provide links for Multivariate2018, MIMIC, StackOverflow, BookOrder, Synthetic, Neonate and traffic. There is also code provided for synthetic data generation. Citations are provided in 4.3. Datasets are described in detail (including synthetic generation formula) in C.3.2. Statistics are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state hyperparameter optimisation is done in the implementation readme. An ablation study is done in the appendix. Parameter values can be found in the example scripts of the readme, but a full overview is missing and its a bit unclear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use accuracy and ranking as metrics in table 3, they average over the datasets. In table 4 they present the results log likelihood, accuracy and RMSE over 4/5-fold cross validation and repeated 3 times reporting the mean and std dev.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise in time series data and transformers.
