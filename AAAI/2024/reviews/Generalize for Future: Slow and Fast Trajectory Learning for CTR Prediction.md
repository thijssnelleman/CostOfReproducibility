
## Generalize for Future: Slow and Fast Trajectory Learning for CTR Prediction
Jian Zhu, Congcong Liu, Xue Jiang, Changping Peng, Zhangang Lin, Jingping Shao
Keywords: APP: Web, ML: Applications
AAAI/2024/Proceedings/27626 - Generalize for Future: Slow and Fast Trajectory Learning for CTR Prediction.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not provide a source code repository. They do note some design choices for their implementation and provide a pseudo code algorithm in their paper regarding the training procedure. The authors do not state which frameworks/programming languages were used but they could perhaps be derived from their citations.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use a dataset from Kaggle with descriptions on the data, another data set from Taobao and Cikm2019 data set including links where they can be found.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors note details on the hyperparameters and architecture in the baseliens and implementation details subsection. They note the values used for key values and state that a search was conducted, but not how this was done, over several parameters for each method on the datasets, but refer to the non-included appendix for more details. This cost could have been lowered by providing implementation documentation and AAAI including the appendix.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state how the data was divided for training/testing purposes and state more details are available in the appendix which AAAI does not include. The authors describe the used evaluation metrics. The number of runs (3) is only noted shortly in the results paragraph, but not how these runs handle the data split, indicating it was static. This cost could have been lowered by clarifying this and AAAI including appendix.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The authors present extensive documentation on their proposed frame work and the mechanisms and include two short illustrations. It is a complex concept and requires some understanding of trajectory data/tasks. 
