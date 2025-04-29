
## Simple and Efficient Heterogeneous Graph Neural Network
Xiaocheng Yang, Mingyu Yan, Shirui Pan, Xiaochun Ye, Dongrui Fan
Keywords: ML: Graph-based Machine Learning, DMKM: Graph Mining, Social Network Analysis & Community Mining
AAAI/2023/Proceedings/26283 - Simple and Efficient Heterogeneous Graph Neural Network.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/ICT-GIMLab/SeHGNN). In the readme the authors provide requirements, and how to prepare data (and where to download it from). The code has a decent amount of comments, and the authors state where they lend code from. Some files/functions can run a bit long, but in general the repository has a good structure. In the method the authors provide pseudo code on the training procedure and two large detailed architecture schematics. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors present download instructions on the data in the implementation documentation and provide code/details on data loading and preparation. One data set should even download automatically when running for the first time. In the paper the authors state they use 4 benchmark data sets and provide a description and citations. In the linked appendix the authors state statistics on the datasets used and provide more details regarding the method on each data set. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide a link to their appendix (https://arxiv.org/abs/2207.02547). There are some details recorded there regarding the method and the values of key hyperparameters are stated there. Possibly missing values could be extracted from the implementation. A full table regarding the hyperparameter settings per method/task would be welcome. No details are given how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use commonly used metrics, but a short description on them would still be welcome. Details regarding train/test splits are given in the appendix. There they also state what they average over how many runs, but how this exactly translates to the results presented requires a bit of subdomain specific expertise. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding of geometric deep learning. 
