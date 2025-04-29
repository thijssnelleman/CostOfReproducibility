
## Detecting Corrupted Labels Without Training a Model to Predict
Zhaowei Zhu, Zihao Dong, Yang Liu
Keywords: 
ICML/2022/Proceedings/17021 - Detecting Corrupted Labels Without Training a Model to Predict.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/UCSC-REAL/SimiFeat). In the readme they post updates, installation instructions, how to run the code and a link to a library their method is now a part of. The code has an acceptable amount of comments. The repository structure could use some explanation but its just small enough to remain overseeable. The fact that they published their method in a package is very helpful for re-implementation. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

There are some automatic downloaders in the implementation for CIFAR-10 and CIFAR-100. The authors state they use CIFAR in section 5 but also Colthing 1M in appendix C. On both citations are provided but no descriptions/statistics. The authors use models pretrained on ImageNet but not the data set itself. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors discuss hyperparameter values in section 5. They state there are two. They reason ghow they set these values in their experiment (empircally) but not under what budget this was acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate F1 scores over CIFAR-10 and CIFAR-100. In table 4 they evaluate top-x accuracy over the test set of clothing1m. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires experience with corrupted data detection. 
