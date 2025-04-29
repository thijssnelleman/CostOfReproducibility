
## Coordinate Descent on the Orthogonal Group for Recurrent Neural Network Training
Estelle Massart, Vinayak Abrol
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20742 - Coordinate Descent on the Orthogonal Group for Recurrent Neural Network Training.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The implementation is posted online (https://github.com/EMassart/OrthCDforRNNs). The readme contains a description on the method, an introduction regarding what of their algorithm is implemented where and which file to execute to replicate the results for the copying task. The repository only consists of 2 files, and both are relatively short, well commented and easy to understand. Some static variables could have been parametrisable, however this should not have any impact on the re-implementation. The authors provide two pseudo code pieces on their method too. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors source their data from a generative problem, for which they state the border/parameters.  They source the code for this from another repository and link it. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors use a model and its architecture from a previous work and provide the source to it. The hyperparameters for this model can be found in the code, and the authors state they rely on their implementation. Their own method is seemingly hyperparameter free, based on the pseudo code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state for how many epochs the method is run on the problem, and evaluate the training loss over them. There is no train/test applicable here, so the experiment is very straightforward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

The method requires an extreme understanding of loss functions and optimization in neural networks, and especially the mathematics regarding gradients.
