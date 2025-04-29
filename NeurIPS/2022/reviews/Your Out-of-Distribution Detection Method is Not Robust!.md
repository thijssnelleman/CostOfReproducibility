
## Your Out-of-Distribution Detection Method is Not Robust!
Mohammad Azizmalayeri, Arshia Soltani Moakhar, Arman Zarei, Reihaneh Zohrabi, Mohammad Manzuri, Mohammad Hossein Rohban
Keywords: 
NeurIPS/2022/Proceedings/53795 - Your Out-of-Distribution Detection Method is Not Robust!.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

Implementation is provided in the supplementary material (https://proceedings.neurips.cc/paper_files/paper/2022/file/1f6591cc41be737e9ba4cc487ac8082d-Supplemental-Conference.zip). Readme introduces the method, provides installation instructions, where to download the datasets all with direct links, details on how to run training with parameter descriptions and acknowledgements of other repositories they used for inspiration. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(12/12)

Dataset used is CIFAR-10 and CIFAR-100 as in distribution datasets, and eight datasets for OOD namely MNIST, TinyImageNet, Places365, LSUN, iSUN, Birds, Flower, COIL-100 as test sets and SVHN as validation set and Food-101 as open training set. Citations provided for all. Links in implementation. No descriptions or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values per experiment are stated in the readme and summarised in section 4.1. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metric used is AUROC. Results are over datasets and their roles assigned in 4.1. Results are averaged over the datasets. No variance.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on OOD robustness.
