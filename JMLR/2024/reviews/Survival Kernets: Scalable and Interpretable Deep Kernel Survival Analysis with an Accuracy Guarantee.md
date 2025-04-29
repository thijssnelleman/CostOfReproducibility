
## Survival Kernets: Scalable and Interpretable Deep Kernel Survival Analysis with an Accuracy Guarantee
George H. Chen
Keywords: 
JMLR/2024/Proceedings/220667 - Survival Kernets: Scalable and Interpretable Deep Kernel Survival Analysis with an Accuracy Guarantee.pdf
Project URL: https://github.com/georgehc/survival-kernets

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to the implementation on the JMLR website (https://github.com/georgehc/survival-kernets) and is also provided in the abstract. In the readme they state a description on the code development, installation requirements, download links for the datasets, how to run code with lengthy descriptions and an example description and where to find it. Code has okay comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors provide download links in the implementation as well as in footnote 1. There are brief descriptions on each and statistics in sec 5 / table 5.1. Only UNOS has no download link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors details hyperparameter and optimization in appendix C.2. Here htey provide the grids that were optimised (grid search). Configuration file available with final results in the implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors report results with mean + std dev over 5 repeats. Metric is accuracy. Data split is 80/20 and best HP setting is sleected over the validation test. Results are on the test set. Not clear hwere the test set comes from if its split is 80/20.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on survival analysis and NN interpretability and kernel methods.
