
## Towards Practical Control of Singular Values of Convolutional Layers
Alexandra Senderovich, Ekaterina Bulatova, Anton Obukhov, Maxim Rakhuba
Keywords: 
NeurIPS/2022/Proceedings/55307 - Towards Practical Control of Singular Values of Convolutional Layers.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state in section 5 the implementation was done in PyTorch (citation provided). They provide a link to the implementation in the abstract (https://github.com/WhiteTeaDragon/practical_svd_conv). In the readme they state installation instructions, details on logging, how to train with details and various aparameters, how to compute metrics. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use CIFAR-10, CIFAR-C and CIFAR-100 (citations provided). They download automatically in the code. No description or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters per experiment are given in the readme and in a file in the implementation. They are also discussed in section 5. Acquisition not completely clear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metric are various types of accuracy and expected calibration error (ECE, cited but not explained). Aggregation and variation not explained. Results are on the Test split or Cifar-C dataset. Results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise in robustness and CNNs.
