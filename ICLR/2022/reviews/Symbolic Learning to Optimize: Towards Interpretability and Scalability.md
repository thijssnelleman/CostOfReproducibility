## Symbolic Learning to Optimize: Towards Interpretability and Scalability
Wenqing Zheng, Tianlong Chen, Ting-Kuei Hu, Zhangyang Wang
Keywords: 
ICLR/2022/Proceedings/6741 - Symbolic Learning to Optimize: Towards Interpretability and Scalability.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/VITA-Group/Symbolic-Learning-To-Optimize). In the readme they state an intro to the method and findings, how to install, how to run training code with an explanation of the parameters, index of what code can be found where. The code varies strongly in quality of comments. There are mor examples in the other readmes of the repository which do help.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use CIFAR10 and CIFAR100 but provide few details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors motivate hyperparameter values in appendix C. and some are listed in text with grids in section 4. No structured overview.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure accuracy on the test set (static split) over single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
