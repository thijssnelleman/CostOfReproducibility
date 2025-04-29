
## Distribution Alignment Optimization through Neural Collapse for Long-tailed Classification
Jintong Gao, He Zhao, Dandan Guo, Hongyuan Zha
Keywords: 
ICML/2024/Proceedings/34453 - Distribution Alignment Optimization through Neural Collapse for Long-tailed Classification.pdf
Project URL: https://github.com/JintongGao/DisA

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/JintongGao/DisA). In the readme the authors state the installation requirements, examples on how to run the code regarding training/evaluation, and acknowledgements regarding other repositories used to create this implementation. Only one of the code files has a lot of comments, the rest is seemingly without. The repository structure is easy to oversee. The implementation details are summarised in 5.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors state the data sets used in 5.1, with citations. They explain how these variants were derived from the original datasets. There are no task descriptions or dataset statistics given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Various hyperparameter values are stated in the implementation details paragraph. More hyperparameter values are detailed in the appendix, and they also analyse the impact of the HP delta and a grid evaluation of HP p. The hyperparameters of their method are summarised in appendix D algorithm 2. A summary on it is given in table 8 and 9 as well. No acquisition procedure specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state they report the average of three repeated experiments over varying seeds. They report accuracy over various subsets of the test set that they specify. However it is not documented how the datasets are split up into training and testing data. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on imbalanced data classification/loss functions and general training procedures of NNs.
