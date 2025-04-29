
## Bayesian Cross-Modal Alignment Learning for Few-Shot Out-of-Distribution Generalization
Lin Zhu, Xinbing Wang, Chenghu Zhou, Nanyang Ye
Keywords: ML: Transfer, Domain Adaptation, Multi-Task Learning, CV: Applications, CV: Language and Vision, CV: Multi-modal Vision, CV: Representation Learning for Vision, ML: Applications, ML: Deep Neural Network Algorithms, ML: Meta Learning, ML: Multimodal Learning, ML: Other Foundations of Machine Learning, ML: Representation Learning
AAAI/2023/Proceedings/26355 - Bayesian Cross-Modal Alignment Learning for Few-Shot Out-of-Distribution Generalization.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/LinLLLL/BayesCAL). The authors provide installation notes regarding the envorinment set up, a data set download link for CCD, a general structure of the data directories is explained, a short explanation on how the code can be run, and the schematic of the pipeline. Lastly, the authors note a results collection script. The code has some comments here and there, however there are files completely without comments. In general the implementation is well documented. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

There are data loaders present for each data set in the implementation. The authors discuss 4 data sets and their references in the paper. Only colored cats and dogs seems to have no citation but does have a direct download link in the implementation. No statistics on the data sets are presented. There are no download links specified for the other data sets, but do note they are publicly available in the implementation. There are more datasets presented in the implementation than discussed in the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors discuss hyperparameters in the experimental protocol. They denote these values later on. The authors also state they did a 20 shot random search of hyperparameter values. The full configurations can be found per model in the implementation documentation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors clearly state their experimental protocol regarding training and testing, and the metrics reported are discussed. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The authors deal with few shot learning, and introduce their solution with clear illustrations. Although some other resources should help with a complete understanding, with the clear documentation provided including the implementation, the authors have clearly minimised this cost.
