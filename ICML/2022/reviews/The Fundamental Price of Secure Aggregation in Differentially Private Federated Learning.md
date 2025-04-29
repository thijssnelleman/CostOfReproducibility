
## The Fundamental Price of Secure Aggregation in Differentially Private Federated Learning
Wei-Ning Chen, Christopher Choquette Choo, Peter Kairouz, Ananda Suresh
Keywords: 
ICML/2022/Proceedings/17529 - The Fundamental Price of Secure Aggregation in Differentially Private Federated Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their code online (https://github.com/google-research/federated/tree/master/private_linear_compression). In the readme the authors state the installation dependencies, how to run the code and visualise the output, explanation on the possible parameters and tips on trouble shooting. The comments in the code are amazing. Pseudo code is available in algorithm 1 and 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors state the three datasets they use in the experiments in section 7 with a citations, and a statistical description and a longer one in appendix C. Two datasets have a direct link in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in appendix C with model architectures. An overview of all parameters is available in the code. No acquisition method specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate test accuracy of the models over various compression rates. The variation is over the number of clients, and they take the mean but the variation itself in fig 2b is not clear. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in federated learning and differentially private learning.
