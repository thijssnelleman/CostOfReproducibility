
## Gradient Flow in Sparse Neural Networks and How Lottery Tickets Win
Utku Evci, Yani Ioannou, Cem Keskin, Yann Dauphin
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20611 - Gradient Flow in Sparse Neural Networks and How Lottery Tickets Win.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/google-research/rigl/tree/master/rigl/rigl_tf2). In the readme they provide a brief introduction to the method, how to run pruning, training and how to adapt the settings, run experiments, and a step wise explanation how to use them together. There is also a jupyter notebook as an example. The code is well documented with comments and the configurations are stored in seperate files. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three data sets and three models for their experiments. The data sets are easily recognisable as popular benchmark data sets, but citations and details on them are missing. For the models citations are given. The authors source the data directly from tensorflow in their implementation so their accesibility is very high when using their code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

A few configuration values are discussed but not to great extent. Their full values are available in the implementation docs. No acquisition strategy is specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors do not explicitly state their procedure. Details can be inferred from table 1 caption, and the general presentation of the method, but no statements are made on how the data is divided into train/test for example, but that can be extracted from the implementation. They state 'mutliple runs' for their variance, but not how many there are. The metrics are well explained. A short paragraph summarising these details (in the paper or the implementation) would be welcome.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a very good understanding on neural network pruning and sparse neural networks.
