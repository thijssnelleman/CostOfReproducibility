## Internal Cross-layer Gradients for Extending Homogeneity to Heterogeneity in Federated Learning
Yun-Hin Chan, Rui Zhou, Running Zhao, Zhihan JIANG, Edith Ngai
Keywords: 
ICLR/2024/Proceedings/19167 - Internal Cross-layer Gradients for Extending Homogeneity to Heterogeneity in Federated Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

Authors provide implementation URL in footnote 3 of section 5 (https://github.com/ChanYunHin/InCo-Aggregation). Readme has an overview of the method, installation instructions, two example commands to execute, other repos used to build this one. Comments are good.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

Fashion-MNIST, SVHN, CIFAR-10, CINIC-10, all cited. Download automatically in code. No other details. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HPs detailed in appendix H.2. Alpha parameter evaluated on two values. No structured overview. No acquisition.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

Authors measure test accuracy, averaged over 3 random seeds, var not clear. Split not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
