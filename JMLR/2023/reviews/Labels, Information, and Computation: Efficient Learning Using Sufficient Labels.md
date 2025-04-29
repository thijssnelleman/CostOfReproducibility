
## Labels, Information, and Computation: Efficient Learning Using Sufficient Labels
Shiyu Duan, Spencer Chang, Jose C. Principe
Keywords: 
JMLR/2023/Proceedings/220019 - Labels, Information, and Computation: Efficient Learning Using Sufficient Labels.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(5/5)

In section 6 the authors conduct experiments on MNIST, FMNIST, SVHN, CIFAR-10 and CIFAR-100 (All have citations). No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors used the validation set for tuning HPs. No other details given on the hyperparameters. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the training set sizes per dataset in 6.1 and how they created the validation set from it. They also state they report the performance for all datasets on the standard test set (thus also standard training split implied). The authors report mean + std dev over 5 trials. Metric is accuracy. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on efficient learning as well as practical experience as a lot of details are missing.
