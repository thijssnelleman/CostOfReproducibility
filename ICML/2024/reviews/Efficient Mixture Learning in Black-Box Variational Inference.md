
## Efficient Mixture Learning in Black-Box Variational Inference
Alexandra Hotti, Oskar Kviman, Ricky Molén, Víctor Elvira, Jens Lagergren
Keywords: 
ICML/2024/Proceedings/34484 - Efficient Mixture Learning in Black-Box Variational Inference.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors link their implementation (https://github.com/okviman/efficient-mixtures). The readme has a snippit from the paper and a brief instruction on how to run the training procedure for a specific dataset with some parameter explanations. The code has a decent amount of comments. The repository structure is quite large and could use an index. There is a requirements file regarding installation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(11/11)

The authors use a 'toy example' (synthetic data) which they provide in their code. The authors use two benchmark datasets with descriptions and citations provided in appendix D. On the eight phylogenetic datasets only citations are provided. There are no direct links present.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

There is no clear summary on the methods hyperparameters. They can be extracted from the implementation with some difficulty. Some pipeline parameters are specified in table 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use NLL (negativive log-likelihood), learnable parameters and time as metrics. The results are single configuration/model. Train/test splits are not completely clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires experience in with variational auto encoders, and bayesian inference. 
