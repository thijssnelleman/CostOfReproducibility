
## Generalizable Person Re-identification via Self-Supervised Batch Norm Test-Time Adaption
Ke Han, Chenyang Si, Yan Huang, Liang Wang, Tieniu Tan
Keywords: Computer Vision (CV), Machine Learning (ML)
AAAI/2022/Proceedings/19963 - Generalizable Person Re-identification via Self-Supervised Batch Norm Test-Time Adaption.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not provide a source for their implementation. They state in their implementation some details on how it was trained including hyperparameters, and state the experiments were conducted with PyTorch. A detailed illustration is available on the framework, and a smaller one regarding training/testing. Pseudo code on a part of their algorithm is given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors construct a training set by taking 5 data sets and provide citations on them. The test sets are listed too and also include small statistics. There is no direct link provided to the data sets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters are given in the implementation details and are quite detailed. It will take some effort to verify that all necessary parameter values are given but it does look complete. No details are given on acquisition strategy or budget. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors cite their evaluation protocol, provide a description on their metrics, and how many runs were conducted and that the splits were randomised. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The presented method is quite complex, and although well explained it requires previous experience in depth with various deep learning techniques. The absence of the implementation means independent investigators have less example material to work with, which raises the amount of expertise required to reproduce the work.
