
## Implicit Graph Neural Networks: A Monotone Operator Viewpoint
Justin Baker, Qingsong Wang, Cory Hauck, Bao Wang
Keywords: 
ICML/2023/Proceedings/24645 - Implicit Graph Neural Networks: A Monotone Operator Viewpoint.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/Utah-Math-Data-Science/MIGNN). The authors state in the readme the installation instructions, links to download the datasets (some through a lib), how to run numerical simulations and some options explanations with mathematical formulas. The code could use some more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(9/9)

The authors provide download instructions for various datasets. The authors use 5 graph classification benchmarks, 3 other graph benchmarks and synthetic chain (which they cite) and provide details on in Appendix I. More data set statistics can be found in table 4. All datasets are available through the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the tuned hyperparameters in table 5, and provide the search strategy in appendix section J. They state the selected values per dataset in table 6, 7, and 8. The budget is not exactly clear but can be deduced from the paper and the implementation (or atleast approached).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the mean accuracy with standard deviation over 10 fold cross validation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires experience in GNNs and geometrical deep learning. 
