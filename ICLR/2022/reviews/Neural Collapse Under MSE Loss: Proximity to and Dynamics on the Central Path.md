## Neural Collapse Under MSE Loss: Proximity to and Dynamics on the Central Path
X.Y. Han, Vardan Papyan, David Donoho
Keywords: 
Award: Outstanding Paper Award
ICLR/2022/Proceedings/683 - Neural Collapse Under MSE Loss: Proximity to and Dynamics on the Central Path.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their code in the abstract (https://colab.research.google.com/github/neuralcollapse/neuralcollapse/blob/main/neuralcollapse.ipynb). The code has nice comments, although the authors could have made more use of the notebook. The versioning is handled by Google Colab, but specifications would be welcome incase something breaks.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use the MNIST, FashionMNIST, CIFAR10, SVHN, and STL10 datasets and provide citations for all. Some motivation is given in A.1. Few other details on the datasets are provided. Links are not provided in the notebook (Runs on MNIST-ResNet18). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

The authors refer to a previous work regarding the hyperparameter optimisation. Some values can be found in the notebook. It will require some investigation to determine the used values and how they were acquired.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure accuracy of the training procedure over single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
