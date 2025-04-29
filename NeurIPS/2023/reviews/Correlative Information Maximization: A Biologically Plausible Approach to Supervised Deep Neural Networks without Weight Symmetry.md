
## Correlative Information Maximization: A Biologically Plausible Approach to Supervised Deep Neural Networks without Weight Symmetry
Bariscan Bozkurt, Cengiz Pehlevan, Alper Erdogan
Keywords: 
NeurIPS/2023/Proceedings/71555 - Correlative Information Maximization: A Biologically Plausible Approach to Supervised Deep Neural Networks without Weight Symmetry.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their implementation online (https://github.com/BariscanBozkurt/Supervised-CorInfoMax). In the readme they describe the method and provide various details on which parts of the code is responsible for what. There is a requirements file for installation. Could use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use MNIST, FashionMNIST and CIFAR10 as datasets. The datasets are cited but no descriptions/statistics. The datasets download automatically in their implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are fully specified per datasets in table 3 of appendix J.4.2. and described in table 2 but acquisition is not specified. (Full paper see arxiv)

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present test set accuracy results with mean ~+ std dev over 10 runs. The test sets are static/provided, but is not excplitly stated. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on biological neural networks.
