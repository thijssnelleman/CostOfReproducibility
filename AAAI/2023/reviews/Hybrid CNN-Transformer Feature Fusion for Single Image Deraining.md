
## Hybrid CNN-Transformer Feature Fusion for Single Image Deraining
Xiang Chen, Jinshan Pan, Jiyang Lu, Zhentao Fan, Hao Li
Keywords: CV: Low Level & Physics-Based Vision, CV: Applications, CV: Computational Photography, Image & Video Synthesis, CV: Representation Learning for Vision
AAAI/2023/Proceedings/25111 - Hybrid CNN-Transformer Feature Fusion for Single Image Deraining.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a source of their implementation (https://github.com/cschenxiang/HCT-FFN). In the readme, they provide a network architecture, installation requirements/dependencies, training instructions, testing instructions and some references on how they computed the results. They also link the source on which they based their code. The code itself has very few comments. Although the repository is complete, it could do with better documentation in general.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors use five public data sets, which they dicsuss with some key statistics and provide citations on. There is no direct link on where to find the downloadable data set.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide hyperparameter values in the implementation details section. A large list of options can be found in the implementation documentation with default values, so it can be checked if all hyperparameters needed are given. There is no information on how these values were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide details on the evaluation metrics and how the data is divided for training and testing. They prsent single model/run results. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method's task is somewhat specific and requires some expertise to understand the problematics with it. The authors present a complex method, but it is well documented. 
