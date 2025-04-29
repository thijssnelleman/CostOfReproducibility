
## A Graph Convolutional Network with Adaptive Graph Generation and Channel Selection for Event Detection
Zhipeng Xie, Yumin Tu
Keywords: Speech & Natural Language Processing (SNLP)
AAAI/2022/Proceedings/21405 - A Graph Convolutional Network with Adaptive Graph Generation and Channel Selection for Event Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. The model architecture is presented in figure 3, a modular structure in figure 2 and how it diverts from traditional methods. Some examples are given. No implementation details are specified.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors provide statistics and description on the data set. No link is provided nor a citation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors simply state they tune the HPs using the development set, suggesting ('we tune them') 'human search'. They state the values of their used configuration, but its hard to verify if all needed values are presented for reproduction. No budget is stated for acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state how the data split is done for training, development and test set (static). They state the metrics used, and how many runs and how they are aggregated. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in geometric deeplearning / graph neural networks and the task evaluated in the paper (NLP). 
