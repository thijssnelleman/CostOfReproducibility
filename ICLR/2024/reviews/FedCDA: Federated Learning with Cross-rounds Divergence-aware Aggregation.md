## FedCDA: Federated Learning with Cross-rounds Divergence-aware Aggregation
Haozhao Wang, Haoran Xu, Yichen Li, Yuan Xu, Ruixuan Li, Tianwei Zhang
Keywords: 
ICLR/2024/Proceedings/17851 - FedCDA: Federated Learning with Cross-rounds Divergence-aware Aggregation.pdf
Project URL: https://openreview.net/attachment?id=nbPGqeH3lt&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors state in 6.1 they use PyTorch 2.0 for the implementation. The code is provided in the supplementary materials (https://openreview.net/attachment?id=nbPGqeH3lt&name=supplementary_material). There is no readme, but there are requirements.txt files describing used dependencies with versions in each directory. The code has quite alot of comments, albeit in mandarin (Whereas it would be prefered that all documentation is in the same language). 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

Fashion-MNIST, CIFAR-10 and CIFAR-100  (all cited). No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

HP values summarised in text in 6.1. Config files provided in the implementation. Some HP values are varied and analysed in the paper regarding their method.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Authors measure test accuracy, measured over 2 runs last 10 rounds with average and standard variance. Data split not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
