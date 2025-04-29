
## Privacy for Free: How does Dataset Condensation Help Privacy?
Tian Dong, Bo Zhao, Lingjuan Lyu
Keywords: 
Award: Outstanding Paper
ICML/2022/Proceedings/76 - Privacy for Free: How does Dataset Condensation Help Privacy?.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors link an implementation for reproducing DSA. They state that experiments were conducted in PyTorch 1.10. Their own implementation is not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use 3 datasets in section 5: MNIST, CIFAR-10 and CelebA (all with citation). No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state they use a three layer CNN in sec 5.1. and refer to a previous work for it. For the settings they state they evaluate the ripc parameter on 2-3 settings as it is important. Other HP settings found in E.1. No other details and no overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Authors present ROC curves, accuracy barcharts and accuracy over varying the ripc parameter. The authors state how the data is split in 5.1 and report results on the test set. Procedure is repeated with 10 random seeds. Results presented with average and standard variance.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on privacy and data set condensation.
