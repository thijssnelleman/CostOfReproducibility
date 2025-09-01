## Learning Strides in Convolutional Neural Networks
Rachid Riad, Olivier Teboul, David Grangier, Neil Zeghidour
Keywords: 
Award: Outstanding Paper Award
ICLR/2022/Proceedings/969 - Learning Strides in Convolutional Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in footnote 1 at the end of the introduction (https://github.com/google-research/diffstride). The readme has an overview on the method, installation notes, examples how to run the code, summary of the results, details regarding CPU/GPU usage and citation details. The code has a lot of comments. The structure is easy to oversee.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use CIFAR10, CIFAR100 and ImageNet (Citations provided). A few key details on the datasets are given and the code seems to download the datasets automatically. General overview/statistics on datasets are not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The hyperparameter values are summarised in 3.2. and structured given in the examples directory using Gin files. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use the official train/test splits of the datasets. The authors report accuracy on the test sets over three runs with std dev. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
