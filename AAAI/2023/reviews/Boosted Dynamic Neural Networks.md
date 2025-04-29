
## Boosted Dynamic Neural Networks
Haichao Yu, Haoxiang Li, Gang Hua, Gao Huang, Humphrey Shi
Keywords: ML: Deep Neural Architectures, ML: Learning on the Edge & Model Compression
AAAI/2023/Proceedings/26302 - Boosted Dynamic Neural Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide their repository link (https://github.com/SHI-Labs/Boosted-Dynamic-Networks). The readme hast a short introduction and diagram of the method, followed by results of the method. There is a short note on where to find model training and evaluation scripts and 'where' to place the data set. They also state which other repositories their work is built on. In the paper they provide some more diagrams, a pseudo code pipeline for training and a few notes on the implementation. The code has barely any comments or explanations whatsoever. Reverse engeneering would be required to understand how it works, thus raising the cost. The authors could have easily lowered this by providing a complete read me and comments in the code. A directory structure explanation would be welcome as well.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use two public datasets and cite their sources. They are very well known, however some description on them and their statistics would be welcome. A link to their source could have been provided in the implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameter values are given for each data set and model combination. Although some values could be lacking, they can be determined from the implementation with some effort. No details are given on how these values are acquired except for RANet where they state they use the settings from the original work. The authors could have provided configuration files to make lives easier.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The training procedure is well explained. The authors seem to present single model results although this need some effort to verify.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires an understanding on neural network procedures, specifically the subset they apply here are early exiting dynamic NN's.
