
## Principled Out-of-Distribution Detection via Multiple Testing
Akshayaa Magesh, Venugopal V. Veeravalli, Anirban Roy, Susmit Jha
Keywords: 
JMLR/2023/Proceedings/230838 - Principled Out-of-Distribution Detection via Multiple Testing.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide pseudo-code in algorithm 1. In appendix E they state the framework used (PyTorch).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/4)

The authors use CIFAR10, SVHN, LSUN, ImageNet. No citations or other details provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state their method in algorithm 1 where they state  input parameter conditional probability alpha with range. Alpha is theoretically guaranteed in section 3 and evaluated as a metric in figure 3. The authors use pretrained architectures ResNet34 and DenseNet and provide citations, HPs not applicable (not their method). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the datasets with in and out of distribution and define the setup per experiment. The Mahalanobis and gram scores are defined in eq 27-31 and calculated 4/5 times per layer in the model which are presented in figure 3. There is some expertise required to fully understand the evaluation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on OOD.
