
## Boulevard: Regularized Stochastic Gradient Boosted Trees and Their Limiting Distribution
Yichen Zhou, Giles Hooker
Keywords: 
JMLR/2022/Proceedings/210078 - Boulevard: Regularized Stochastic Gradient Boosted Trees and Their Limiting Distribution.pdf
Project URL: https://github.com/siriuz42/boulevard

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on JMLR and footnote 2 (https://github.com/siriuz42/boulevard). In the readme they state requirements for the code, how to train with an explanation of the arguments, what the output is and code explanations. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors conduct an empirical study in section 6 and use simulated data and provide the functions and parameters, code is available. They also conduct experiments on four datasets of the UCI repository and provide citations + link and each dataset is named but no other details given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors use a learning rate λ, which they evaluate on a grid of three for the first synthetic experiment and provide the resulting value. For each experiment they state the values in table 1 of appendix B. Acquisition for the real datasets λ not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use train and test sets which are specified in 6.1. For the real datasets the authors present the average over 5-fold cross validation. Figure 7 shows boxplots over various sample sizes of the simulator, figure 8 on the real world datasets measuring predicted values. Metrics are not completely clear and require expertise on the task/problem. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on SGD and boosted trees.
