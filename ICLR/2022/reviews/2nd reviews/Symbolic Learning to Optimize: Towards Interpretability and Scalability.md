## Symbolic Learning to Optimize: Towards Interpretability and Scalability
Wenqing Zheng, Tianlong Chen, Ting-Kuei Hu, Zhangyang Wang
Keywords: 
ICLR/2022/Proceedings/6741 - Symbolic Learning to Optimize: Towards Interpretability and Scalability.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

[Public repo is available (https://github.com/VITA-Group/Symbolic-Learning-To-Optimize), with clear instructions how to install and execute the code for different experiments, with accompanying exampls. Repo is easy to navigate, however the code itself is overall poorly commented (+1).]

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

[Datasets used are very standard: MNIST, CIFAR-10 and CIFAR-100. No links, no description nor statistics in the paper, but since the datasets are so widely used and well known, I wouldn't increase the score by the total suggested amount, which would be +5. Link to CIFAR-10 is available in the repo; for CIFAR-100 and MNIST links are not provided. The collection strategy is missing, as it is not clear how CIFAR100 was used. Total cost of 4]

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

This section is tricky. There are some hyperparameters that are outlined in the text, but no proper HPO strategy seems to have been used. It is not clearly documented how those were obtained. It looks to me more like a sensitivity analysis on the values of HPs, and not HPO. For symbolic regression, there are more details in Appendix C, but they are not systematically presented. It's hard to pinpoint the exact cost, but the penalty is high for this section. I would go for at least 5.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[5]

Metrics that are used are standard accuracy and R2 score. Other metrics are novel, introduced and defined by authors. I could not find info on train/test splits in paper nor repo (+2). It is implied that all methods were run once (+1). The proposed method was tested over different random seeds and showed no variance, but it is not clearly stated whether this also holds for the main experiments(+1).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

[Reproducing the work requires knowledge of genetic programming through symbolic regression and use of standard neural network training schemes. The methodology should be relatively easy to set up again, but reproducing the exact experimental resuls seems to be harder due to some crucial info missing, such as train/test splits.]
