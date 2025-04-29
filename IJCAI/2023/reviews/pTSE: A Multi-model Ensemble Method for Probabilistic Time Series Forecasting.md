
## pTSE: A Multi-model Ensemble Method for Probabilistic Time Series Forecasting
Yunyi Zhou, Zhixuan Chu, Yijia Ruan, Ge Jin, Yuchen Huang, Sheng Li
Keywords: Machine Learning: ML: Probabilistic machine learning, Machine Learning: ML: Time series and data streams
IJCAI/2023/Proceedings/0521 - pTSE: A Multi-model Ensemble Method for Probabilistic Time Series Forecasting.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not publish their implementation. No details on the implementation are shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(3/4)

The authors apply the method to publicly available datasets. First they discuss synthetic data, for which they state the distribution descriptions regarding the generation but do not provide the implementation. Secondly they use three benchmark data sets for which they present a link on one (solar), a citation on another (traffic), but one has no links at all (energy). They provide brief descriptions on them. A lot of information is left to the independent investigators to find out.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The method seems to be parameter free, but this will require some experience /time to verify due to the absent implementation (They do state its a semi-parametric method).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used in section 4.2 and reference a previous work on it. The results seem to be single model/run, but this is not clearly stated. The authors also state the model is evaluated on a test set but its not clear what the division/source of this is.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries a lot of previous experience with ensemble methods as the method would have to be reimplemented without any example from the mathematical descriptions.
