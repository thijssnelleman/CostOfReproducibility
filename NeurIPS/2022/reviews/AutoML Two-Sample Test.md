
## AutoML Two-Sample Test
Jonas M. Kübler, Vincent Stimper, Simon Buchholz, Krikamol Muandet, Bernhard Schölkopf
Keywords: 
NeurIPS/2022/Proceedings/54059 - AutoML Two-Sample Test.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to the implementation in the appendix (https://github.com/jmkuebler/auto-tst). In the readme they state installation instructions, examples how to use the code with customization. Code is well documented. Overview given in figure 1. There is also a seperate implementation regarding the paper experiments on openreview (https://github.com/jmkuebler/autoML-TST-paper). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use CIFAR and MNIST as datasets. Citations are provided. A direct link is in the implementation. Statistics and descriptions are very minor.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors refer for hyperparameters to the settings of the previous work. Their own method (two-sample test) seems to be parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Data split given in sec 5 for all datasets. Each experiment is repeated 5 times. Experiments are over various sample sizes. The variance is one standard error. Aggregation not specified. Metrics are statistical test values.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on automl, data shift and statistical tests.
