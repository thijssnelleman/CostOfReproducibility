
## Weighted Flow Diffusion for Local Graph Clustering with Node Attributes: an Algorithm and Statistical Guarantees
Shenghao Yang, Kimon Fountoulakis
Keywords: 
ICML/2023/Proceedings/838 - Weighted Flow Diffusion for Local Graph Clustering with Node Attributes: an Algorithm and Statistical Guarantees.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation (https://github.com/s-h-yang/WFD). In the readme they state where to find code for a specific experiment in the paper and what code to run to reproduce a specific table from the paper. There are no installation instructions. The code has very few comments. The repository is easy to oversee.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use simulated data for which they explain the generation in section 4.1 with parameters and state the values. The generator is available in the implementation as well as the generated data. The authors also conduct experiments on a benchmark data set which they cite. The data set is available in the repository. There is a short description with statistics on the dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The auhtors define a hyperparameter in algorithm 2. However different parameters are varied between the experiments in figure 1 which are data parameters. The hyperparameter is defined as aformula in section 4.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors define the evaluation metric in 4.1. They evaluate the performance over 100 trials, averaged with standard deviation as variance. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on graph clustering and weighted flow diffusion.
