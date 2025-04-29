
## Towards In-Distribution Compatible Out-of-Distribution Detection
Boxi Wu, Jie Jiang, Haidong Ren, Zifan Du, Wenxiao Wang, Zhifeng Li, Deng Cai, Xiaofei He, Binbin Lin, Wei Liu
Keywords: ML: Deep Neural Network Algorithms, CV: Applications
AAAI/2023/Proceedings/26230 - Towards In-Distribution Compatible Out-of-Distribution Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide no source to their implementation. No details are provided in the paper on their implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(7/7)

The authors use two public data sets and provide a citation on them. They use 5 more data sets (benchmarks) as OOD sources. One more data set is mentioned and cited. No statistics on them are provided. So some details have to be extracted with some effort, and its slightly more work due to the missing implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state a few hyperparameters in the training section, such as learning rate and its schedule. However, other values need to be extracted/determined and with a missing implementation documentation this is quite difficult. They seem to source the values from a previous work.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors clearly state their training set up and provide sources. They state the metrics with a short description, and state which data set will be used for training and which for testing. They use pretrained models and do single runs with them.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a good understanding of statistical distributions and deep neural networks.
