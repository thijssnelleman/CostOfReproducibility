
## Characterizing Out-of-Distribution Error via Optimal Transport
Yuzhe Lu, Yilong Qin, Runtian Zhai, Andrew Shen, Ketong Chen, Zhenlin Wang, Soheil Kolouri, Simon Stepputtis, Joseph Campbell, Katia Sycara
Keywords: 
NeurIPS/2023/Proceedings/70992 - Characterizing Out-of-Distribution Error via Optimal Transport.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their implementation online (https://github.com/luyuzhe111/COT). The readme describes a single code file. There is an installation file present. Code can use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors provide automatics downloading for ColordMNIST, CIFAR10, CIFAR100, RxRx1, Amazon, Camelyon, CivilComments, IWildCamd, ImageNet, Breeds and WILDS datasets. 4 of the used datasets are leveraged from ImageNet/Breeds. Citations are provided for all. Descritpions in appendix C are shallow. Statistics not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values per dataset are summarised in appendix D. Acquisition not specified. They are summarised semi-structured in the code as well. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Experiments were repeated 3 times over specified seeds (appendix D) and averaged. Results are reported on the static tes set of each dataset. Metric is MAE. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on OOD methods.
