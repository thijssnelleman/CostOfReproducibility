
## Event-Aware Multimodal Mobility Nowcasting
Zhaonan Wang, Renhe Jiang, Hao Xue, Flora D. Salim, Xuan Song, Ryosuke Shibasaki
Keywords: Data Mining & Knowledge Management (DMKM)
AAAI/2022/Proceedings/20342 - Event-Aware Multimodal Mobility Nowcasting.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/underdoc-wang/EAST-Net). In their readme they provide brief instructions on how to train and test the model. The data sets are included in the repository, with an illustrations including details on it. Preprocessing scripts are given. The code has very few comments. The repository is not too large making it easy to go through. If the documentation/comments were a bit more extensive this should be 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/4)

The data is included in the implementation documentation, except for one dataset. The authors collected this data themselves and provide extensive statistics/details on them as well as an informative description.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide many hyperparameter values which can easily be checked/applied with the implementation documentation. The authors do not state how this configuration was acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state how the data is dived for training/testing, state which metrics they used (without description but they are very common), The results indicate single run/model results but its not specifically stated. This can be easily verified with the implementation documentation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding of spatio temporal data to understand the task/method.
