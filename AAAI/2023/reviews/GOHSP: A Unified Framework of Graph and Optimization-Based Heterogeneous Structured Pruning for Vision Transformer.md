
## GOHSP: A Unified Framework of Graph and Optimization-Based Heterogeneous Structured Pruning for Vision Transformer
Miao Yin, Burak Uzkent, Yilin Shen, Hongxia Jin, Bo Yuan
Keywords: ML: Applications, ML: Representation Learning, CV: Representation Learning for Vision
AAAI/2023/Proceedings/26298 - GOHSP: A Unified Framework of Graph and Optimization-Based Heterogeneous Structured Pruning for Vision Transformer.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide no link to their implementation. Two pseudo code algorithms are presented in the paper, and an overal procedure illustration. No details on the implementation are given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors conduct experiments on the CIFAR-10 and ImageNet data sets and provide citations on them. They also use dense models as input and provide sources on these too. The model source is given but not directly linked. No details or statistics are provided on the data sets so this would have to be determined by following the sources.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide hyperparameters for their training procedure per data set. No details are given regarding the parameter acquitsion except for the sparsity distribution. It is not directly clear whether all values of the HP space have been given, and would have to be determined by following the source for the model.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors do not state specifically what the experiments procedure is, rather this has to be inferred. It is not clearly stated how training and test sets are acquired.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method presents a framework regarding pruning for vision transformers. This draws expertise from many different domains and would require some expertise on all of them to understand the presented framework.
