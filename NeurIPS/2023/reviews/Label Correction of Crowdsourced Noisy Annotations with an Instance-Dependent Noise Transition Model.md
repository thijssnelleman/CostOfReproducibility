
## Label Correction of Crowdsourced Noisy Annotations with an Instance-Dependent Noise Transition Model
Hui GUO, Boyu Wang, Grace Yi
Keywords: 
NeurIPS/2023/Proceedings/70516 - Label Correction of Crowdsourced Noisy Annotations with an Instance-Dependent Noise Transition Model.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/hguo1728/BayesianIDNT). The readme is basically empty. The code has okay comments. There are no installation instructions. The repository structure is overseeable enough.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use MNIST, CIFAR-10, CIFAR-100, CIFAR-10N and LabelMe as datasets (all with citations), and detail the descriptions in appendix C.1. Extensive statistics are missing. There are no direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors discuss the HP values per dataset in appendix C.1. No structured overview or acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use accuracy as a metric in table 1. They present the results as average test accuracy of 5 random trials with standard error. In figure 2 they present the learning average accuracy over CIFAR-10 with standard deviation as variation over the same variation. In figure 1 they measure the average estimation error (metric defined) on CIFAR 10 with std dev as variation. Train test splits are specified as static/given per dataset in C.1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries expertise on lable correction for noisy annotation.
