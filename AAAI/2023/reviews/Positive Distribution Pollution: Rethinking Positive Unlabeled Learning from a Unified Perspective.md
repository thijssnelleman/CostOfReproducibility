
## Positive Distribution Pollution: Rethinking Positive Unlabeled Learning from a Unified Perspective
Qianqiao Liang, Mengying Zhu, Yan Wang, Xiuyuan Wang, Wanjia Zhao, Mengyuan Yang, Hua Wei, Bing Han, Xiaolin Zheng
Keywords: ML: Semi-Supervised Learning, ML: Deep Generative Models & Autoencoders, ML: Unsupervised & Self-Supervised Learning
AAAI/2023/Proceedings/26051 - Positive Distribution Pollution: Rethinking Positive Unlabeled Learning from a Unified Perspective.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

No source is given regarding their implementation. In the implementation details they mainly specify architecture details, hyperparameters and how the model was trained. They also state more implementation details are in their longer version but this is not linked. The authors provide pseudo code regarding the training process, and an architectural design/schematic. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/3)

The authors provided data set descriptions on the three data sets used. Two of these are public and citations are provided, the third is one the authors collect themselves but provided no link to it so we assume it is not public. Although the description on their own data set is rather short, they do give key statistics on them which can be used for comparison.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Hyperparameter values are provided in the implementation details section. The values are provided and they state they determine the other hyperparameter values through grid search. The size of this grid/number of configurations evaluated is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present their results as mean and std dev over 10 runs. They use F1 and accuracy as metrics and motivate these. In each run the data is re-created. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding of Positive Unlabeled learning to fully reproduce. However the authors provide good examples on it. 
