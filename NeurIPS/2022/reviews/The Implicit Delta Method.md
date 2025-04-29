
## The Implicit Delta Method
Nathan Kallus, James McInerney
Keywords: 
NeurIPS/2022/Proceedings/53915 - The Implicit Delta Method.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide their implementation in footnote 3 (https://github.com/jamesmcinerney/implicit-delta). The readme is empty. The code has few comments. No installation instructions. No file index and the repository/code structure is not too straightforward.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use 1D synthetic data in sec 5.1. and state the generation process with an overview in figure 2. Generator is included in the code. In 5.2 the authors use MNIST and datasets from UCI benchmark (citations provided but nothing else). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Configuration files can be found with parameter values per experiment in the implementation. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

Metrics are run time in seconds, rescaled RMSE of variance, and phi (defined in formula 10). Results are single run. The data splits are not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on epistemtic uncertainty quantification.
