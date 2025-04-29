
## Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization and Equiangular Embedding
Depeng Li, Tianqi Wang, Junwei Chen, Qining Ren, Kenji Kawaguchi, Zhigang Zeng
Keywords: ML: Life-Long and Continual Learning, ML: Time-Series/Data Streams, ML: Classification and Regression, ML: Other Foundations of Machine Learning
AAAI/2024/Proceedings/30358 - Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization and Equiangular Embedding.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors do not provide any source of their implementation. They provide illustrations of their method in the paper and pseudo code, but a general framework schematic is not found. The authors share some details about their implementation in the experiments section, such as what their approach is based on and which library they use (PyTorch). With these details a re-implementation could perhaps be achieved, but it will take some investment.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use three degrees of datasets (small, medium, large) and all of them are described with statistics and cited. They are recognisable as popuplar publicly available benchmark data sets, but with implementation documentation their links could have been provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors clarify that hyperparameters were used as reported in used works, or they use default values. Some values are specified in the experiments section. Budget in this case is looking up (missing) values reported by the cited works.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors run the experiments five times and report the mean and standard deviation on the metrics. It is not clarified which strategy is employed for these five runs regarding the training/testing set, but it seems to indicate the data split was frozen (e.g. no k-fold etc.)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The method is using complex techniques from various domains of mathematics, pushing the required expertise up (involuntarily). The lack of implementation documentation excaserbates this cost, as it would require signficiant resources from independent investigators to reimplement such complex methods. 
