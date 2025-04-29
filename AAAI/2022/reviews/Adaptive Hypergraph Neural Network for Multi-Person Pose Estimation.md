
## Adaptive Hypergraph Neural Network for Multi-Person Pose Estimation
Xixia Xu, Qi Zou, Xue Lin
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/20201 - Adaptive Hypergraph Neural Network for Multi-Person Pose Estimation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors do not share their implementation, but adopt to previous works for their architecture with citations. They state they implemented the experiments in PyTorch. The authors provide illustrations on the process, examples and a design schematic. Although these details will definitely help, it will still take quite the effort to re-implement the method based on this.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three data sets, provide citations on them and two of which can be easily confirmed as public. They provide key details/statistics on them. The source/links to these data sets are not provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the network architecture and the source of them. They state how the networks are initialised and the training procedured per data set. Hyperparameter values are given, but its hard to verify if all needed values are presented. No acquisition method is specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the metrics used for each data set and provide citations them. Only one metric seems non-standard and could have been explained but a citation on it is provided. The train/test divison is given for two data sets, and a third is implied but completely clear. The results and data statement imply single model results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires a thorough understanding of Graph NNs / Graph CNNs to understand the method. An understanding of the presented benchmark tasks is also recommended.
