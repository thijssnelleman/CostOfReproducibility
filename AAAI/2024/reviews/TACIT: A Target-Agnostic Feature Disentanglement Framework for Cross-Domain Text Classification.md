
## TACIT: A Target-Agnostic Feature Disentanglement Framework for Cross-Domain Text Classification
Rui Song, Fausto Giunchiglia, Yingji Li, Mingjie Tian, Hao Xu
Keywords: NLP: Text Classification, NLP: Applications
AAAI/2024/Proceedings/31511 - TACIT: A Target-Agnostic Feature Disentanglement Framework for Cross-Domain Text Classification.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their github (https://github.com/songruiecho/TACIT). The readme is relatively empty and the authors state that "all code will be available soon". The code has some comments in them but is not available, and some are not in english which could complicate things (translations are not always easy). The authors provide a data loader and a link to the data available on github. An architecture design is given in the documentation which can help with understanding their implementation when starting from scratch.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a publicly available data set with four domains and cite the source. A description on the data is given. The URL is provided in the documentation and data loaders are provided in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors denote the values of key hyperparameters of their method, and those lacking can be extracted from the implementation (with some effort). There is no information on how these values were acquired under what budget. They show an analysis of loss functions to support their choice, and present a ablation study on their design choices.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors note in their results table that the results are presented averaged over five folds and state they are measuring accuracy.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method has a clear explanation with a good visualisation, but examples are lacking. This would require more investment for independent investigators to fully grasp the method, which is not persay a bad thing but rather a choice of presenting of the authors.
