## A Simple Yet Powerful Deep Active Learning With Snapshots Ensembles
Seohyeon Jung, Sanghyun Kim, Juho Lee
Keywords: 
ICLR/2023/Proceedings/11592 - A Simple Yet Powerful Deep Active Learning With Snapshots Ensembles.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the abstract (https://github.com/nannullna/snapshot-al). The readme contains examples of how to run the code and there is an installation requirements file present. They also state how the datasets are downloaded and where it needs to be placed. They also state where the configuration files are located per dataset. Code has good comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

CIFAR10 and CIFAR100 download automatically through code, for Tiny Imagenet there is no link. Few details provided, citations present.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

HP values are summarised in appendix B table 8, and a few details on acquisition (human opt, no budget given).

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors report test set accuracies across the datasets and "The reported means and standard deviations were averaged over five trial". Data split is from static dataset splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
