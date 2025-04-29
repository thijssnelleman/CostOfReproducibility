
## Gradient Descent: The Ultimate Optimizer
Kartik Chandra, Audrey Xie, Jonathan Ragan-Kelley, ERIK MEIJER
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/401 - Gradient Descent: The Ultimate Optimizer.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the abstract (https://github.com/kach/gradient-descent-the-ultimate-optimizer). In the readme they state the method, installation notes and an example. Comments are good. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use MNIST, CIFAR-10 and Tolstoy datasets. Citations are provided. No other information.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The baseline alpha value is stated in 3.1. More HP values are stated in table caption 1. They also evaluate over varying hyperparameter values in section 3.1.1., 3.3.2. and 3.4. Acquisition not applicable. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors report the results over 3 runs. Aggregation / variance not specified. It is specified that training and tests sets are used, but not how these were acquired.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on (hyper)optimizers and SGD.
