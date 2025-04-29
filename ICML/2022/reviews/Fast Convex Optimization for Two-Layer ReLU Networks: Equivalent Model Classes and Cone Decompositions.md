
## Fast Convex Optimization for Two-Layer ReLU Networks: Equivalent Model Classes and Cone Decompositions
Aaron Mishkin, Arda Sahiner, Mert Pilanci
Keywords: 
ICML/2022/Proceedings/16549 - Fast Convex Optimization for Two-Layer ReLU Networks: Equivalent Model Classes and Cone Decompositions.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/pilancilab/scnn). In the readme the authors state installation instructions and a link to their readthedocs for the method. There they provide examples and tutorials on the code and a high level overview of the classes/methods/modules in the implementation which are clickable and give more detailed explanations generated from the comments. The method is very well documented. Pseudo code is available in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(22/22)

The authors use MNIST and CIFAR-10 as data sets and a synthetic problem. The distribution of the synthetic classification is given in 5.1. with parameter values. More details are given in appendix D.1. and the generator is available in the code (scnn/src/scnn/private/utils/data). The authors also use 18 UCI datasets for which they provide a citation and a lengthy description on the data sets used in appendix H, which is acceptable due to the number of datasets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state a grid search in appendix H for the regularization parameters and other hyperparameters regarding the random forest clasifier and SVM. The delta parameter is the main parameter of their method and fixed in appendix D.3. A full overview is missing and raises the effort to understand what value should be used when.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present the results as median test accuracies over 5 five fold cross fold validation with first/third quartile in table 7 and single model in table 4. Test set for table 4 is static provided by the source.  In table 1 they present the results as accuracy and runtime as single runs on the test set but this test set is not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on convex optimisation and regularisation. 
