
## Variational Inference for Infinitely Deep Neural Networks
Achille Nazaret, David Blei
Keywords: 
ICML/2022/Proceedings/17237 - Variational Inference for Infinitely Deep Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/ANazaret/unbounded-depth-neural-networks). In the readme they provide details on how to run the code and details of the parameters. They point to code where the main experiments can be reproduced. No installation instructions. The code has very nice comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The implementation has code regarding synthetic data generation, and automatic data downloading for CIFAR-10 but not for UCI but for this there is a direct link in the paper (Additional experiments datasets, not very applicable but described in detail in appendix B). The synthetic data generation is explained with citations in section 6.2, with details in appendix B.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

In footnote 3 the authors explain why not all HPs regarding the models were tuned for their tasks (They want to focus on their method). The hyperparameters are stated in B.2. and B.3. The authors state parameter delta in algorithm 1 which is also stated there and three values are anaylsed in figure 7. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use a train validation and test set and report on the latter for the synthetic data. The results are presented as average + std dev accuracy over 5 runs in table 1. In table 2 test accuracy is reported as well with average + standard deviation over either 3 or 5 runs using the default train-test split of the data set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on variational inference.
