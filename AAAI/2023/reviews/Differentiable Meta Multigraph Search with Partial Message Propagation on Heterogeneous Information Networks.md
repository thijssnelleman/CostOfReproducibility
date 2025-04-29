
## Differentiable Meta Multigraph Search with Partial Message Propagation on Heterogeneous Information Networks
Chao Li, Hao Xu, Kun He
Keywords: ML: Graph-based Machine Learning, ML: Auto ML and Hyperparameter Tuning, ML: Deep Neural Architectures
AAAI/2023/Proceedings/26026 - Differentiable Meta Multigraph Search with Partial Message Propagation on Heterogeneous Information Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their documentation (https://github.com/JHL-HUST/PMMM). They provide a four piece schematic on the readme. There is a list of requirements, and they provide two more readme's for the tasks presented. There direct instructions can be found on how to execute the code. The code has some comments but could do with more / more information rich comments. the architectures are layed out in separate files making it easy to find/understand per dataset. The authors also provide pseudo code in the paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors use data sets for two separate tasks. For the first they use three benchmark data sets and for the second another three. They refer to the appendix for details. Citations on the data sets are not given which could make them slightly more difficult to find. However they do provide direct download links and instructions on the implementation documentation. The appendix is absent due to AAAI limitations. If the appendix was present and the citations were given this cost should be 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors describe key hyperparameter values and some details about random sampling with seeds. For more details they refer to the appendix. Architecture can be found in the implementation docs. Default parameter values regarding training can also be found in the code. It is not 100% clear how these parameter values were found. If the authors had placed the hyperparameter values for each data set / model combination this would have cleared up a lot.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The training procedure and baseline comparison is well described. The results table describes straightforward metrics and they state that they repeat the process with random training seeds 10 times.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method requires some understanding of the tasks and geometrical deep learning, but is in general quite accessible and the implementation documentation serves great examples.
