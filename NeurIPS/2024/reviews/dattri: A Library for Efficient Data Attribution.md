
## dattri: A Library for Efficient Data Attribution
Junwei Deng, Ting-Wei Li, Shiyuan Zhang, Shixuan Liu, Yijun Pan, Hao Huang, Xinhe Wang, Pingbang Hu, Xingjian Zhang, Jiaqi Ma
Keywords: 
NeurIPS/2024/Proceedings/97763 - dattri: A Library for Efficient Data Attribution.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation. In the readme they state their method is a library and its purpose, contents of the readme, how to install with environment setup, how to apply the method with many examples, a list of supported algorithms, supported metrics, supported benchmarks, results and planned work. There is also a documentation website, where the code is detailed with argument descriptions etc. It is extremely well documented.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use MNIST-10, CIFAR-2, Maestro and Shakespeare as datasets. All of them have a link provided in the implementation. There are no descriptions or statistics on the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors benchmark various methods with their framework on the datasets. They state the the search spaces for each method in appendix C.1. The used values are stated in C. The budget is equal to the experimentation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are stated/described in 3.3 with citation. The authors evaluate the methods on the data sets over varying hyperparameters. The training/testing sampling is given in 3.3. Results are single model/run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries expertise on data attribution and some understanding of hyperparameter optimisation.
