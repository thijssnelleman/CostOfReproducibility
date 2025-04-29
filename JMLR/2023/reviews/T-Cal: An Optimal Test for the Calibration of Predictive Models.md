
## T-Cal: An Optimal Test for the Calibration of Predictive Models
Donghwan Lee, Xinmeng Huang, Hamed Hassani, Edgar Dobriban
Keywords: 
JMLR/2023/Proceedings/220320 - T-Cal: An Optimal Test for the Calibration of Predictive Models.pdf
Project URL: https://github.com/dh7401/T-Cal

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website as well as in the abstract and the introduction (https://github.com/dh7401/T-Cal). In the readme they state an overview on the method, motivation, results, how to install, how to reproduce the results and how to contact. The comments are okay.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

In 4.1 the authors conduct an experiment on synthetic data which they describe with parameters and code is provided in the implementation. In 4.2 the authors evaluate on CIFAR-10, CIFAR-100 and ImageNet. No details provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Parameter theoretically analysed, no values used.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors split each provided test set of each dataset into two parts for calibration and testing. The results are presented on the test set with l-ECE scores (Formulae provided). The mis-calibration boolean is explained in 4.1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on uncertainty quantification and calibration.
