## Augmentation with Projection: Towards an Effective and Efficient Data Augmentation Paradigm for Distillation
Ziqi Wang, Yuexin Wu, Frederick Liu, Daogao Liu, Le Hou, Hongkun Yu, Jing Li, Heng Ji
Keywords: 
ICLR/2023/Proceedings/11029 - Augmentation with Projection: Towards an Effective and Efficient Data Augmentation Paradigm for Distillation.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[8]

The authors provide a link to their implementation in the abstract (https://github.com/google-research/google-research/tree/master/augpro) which results in a 404 error. Pseudo code in algorithm 1/2, a few practical details (JAX5, TX5) regarding the implementation are given in appendix C.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use GLUE as a benchmark dataset, citation provided, no other info.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors detail the hyperparameters in appendix C.1. where they state the values in text and the strategy how they were determined (grid). Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors report, Accuracy, Matthew (?), F1, PC/SC. Results on training data, single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
