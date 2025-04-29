
## DFVSR: Directional Frequency Video Super-Resolution via Asymmetric and Enhancement Alignment Network
Shuting Dong, Feng Lu, Zhe Wu, Chun Yuan
Keywords: Computer Vision: CV: Image and video retrieval, Computer Vision: CV: Other
IJCAI/2023/Proceedings/0076 - DFVSR: Directional Frequency Video Super-Resolution via Asymmetric and Enhancement Alignment Network.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state in 4.1 they use the PyTorch framework. The implementation is not shared. The authors state an overview of their method design in figure 2 and an architecture overview in figure 1. This still leaves a lot of implementation work to the independent investigators.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/5)

The authors state they use two widely used datasets for training and provide citations on them, and use a seperate data set for validation and three others for testing, all with citations. The three other data sets are not clearly specified that they are public. No other details/descriptions are given, so a lot of details are left to be figured out by the independent investigators.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state hyperparameter values in 4.1 regarding training. No details regarding the architecture implementation is stated except that they 'develop shallower networks'. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors state in 4.1 how the data sets are used for training/validation/testing. No other details are specified regarding the experiments, and the results imply single model/run results. The authors state the the metrics used in the caption of table 1 but give no explanation on how this was calculated. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in CV, especially a lot of practical experience since a lot of the documentation regarding the experiments (implementation, configuration) is not given.
