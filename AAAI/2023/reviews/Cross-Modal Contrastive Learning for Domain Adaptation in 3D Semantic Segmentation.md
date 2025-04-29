
## Cross-Modal Contrastive Learning for Domain Adaptation in 3D Semantic Segmentation
Bowei Xing, Xianghua Ying, Ruibin Wang, Jinfa Yang, Taiyan Chen
Keywords: CV: 3D Computer Vision, CV: Applications, CV: Multi-modal Vision, CV: Segmentation, ML: Transfer, Domain Adaptation, Multi-Task Learning
AAAI/2023/Proceedings/26525 - Cross-Modal Contrastive Learning for Domain Adaptation in 3D Semantic Segmentation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not provide a link to their implementation source. The authors do provide a small implementation section with some details regards the backbone network and refer to a previous work called xMUDA. A large schematic regarding their method and a large training process diagram are provided which could help re-implementation. However, the general lack of details regarding how their implementation was made severly increase the effort required for re-implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors describe three data sets and provide citations. No statistics are given but the authors do refer to the appendix for more details. They also describe several adaptations done to prepare the data for the tasks, but the implementation is absent, which would require independent investigators to reproduce this in order to defend the comparability which increases the effort.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors provide the hyperparameter values used for training, but it is unclear if these are all the values required due to the implementation docs missing or a full description (in the appendix for example). It is not specified how these values were acquired, the authors do do an ablation study on modules of their method. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors clearly state the evaluation metric. Based on the description of the training procedure, these seem to be single model results, which could have easily been affirmed with the implementation documentation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a good understanding from many cross domain topics. The absence of the implementation gives the independent investigators fewer examples to work with to grasp the method. 
