
## Learning linear non-Gaussian directed acyclic graph with diverging number of nodes
Ruixuan Zhao, Xin He, Junhui Wang
Keywords: 
JMLR/2022/Proceedings/211173 - Learning linear non-Gaussian directed acyclic graph with diverging number of nodes.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors list various packages they use for the implementation in section 7. Pseudo code given in algorithm 1. Their own implementation is not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

In 7.1. the authors use simulated data with three examples with details and parameter values but do not give the implementation. The authors use a COVID-19 dataset for which they provide a direct link and statistics (for example see figure 4). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors specify their method in algorithm 1. Based on the description all the parameters seem to be regarding the input and no performance/semantic parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

For the synthetic examples the authors repeat the generating scheme 50 times and report averaged performance. In table 2 and 3 and figure 3 they present these values with standard error with exact recovery rate, TPR/FDR/MCC/HM/rel-Fnorm as metrics explaind in sec 7. Table 4 gives running times in minutes with average and standard error. For the real data they prsent a visualised result. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on DAG and causal inference.
