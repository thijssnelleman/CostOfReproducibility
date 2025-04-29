
## Right this way: Can VLMs Guide Us to See More to Answer Questions?
Li Liu, Diji Yang, Sijia Zhong, Kalyana Suma Sree Tholeti, Lei Ding, Yi Zhang, Leilani Gilpin
Keywords: 
NeurIPS/2024/Proceedings/96477 - Right this way: Can VLMs Guide Us to See More to Answer Questions?.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide a link to their implementation (https://github.com/LeoLee7/Directional_guidance). Here they provide a link to the data set, otherwise its empty. Framework overview is given in figure 2 and pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

A link to a dataset is given (directional guidance benchmark) in the implementation. In section 4.2 they discuss the dataset that it was created from another dataset which they cite and explain the process of construction. More details are available in A.1. regarding the data set construction and annotator task. Figure 3 has some statistics on the data but more statistics to describe the dataset are expected for a new dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Hyperparameter values are stated in appendix A.2. It is unknown if these are all needed hyperparameters as the implementation is not given. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use F1 score and accuracy as evaluation metrics.  The training dataset is explained in 4.2 but the test set is not completely clear. Results are single model. Figure 4 is a heatmap (no metric) and table 1 is already defined.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on VLMs and A/Q tasks.
