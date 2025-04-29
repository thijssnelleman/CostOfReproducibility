
## Understanding Oversquashing in GNNs through the Lens of Effective Resistance
Mitchell Black, Zhengchao Wan, Amir Nayyeri, Yusu Wang
Keywords: 
ICML/2023/Proceedings/24323 - Understanding Oversquashing in GNNs through the Lens of Effective Resistance.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation online (https://github.com/blackmit/gtr_rewiring). In the readme they provide installation instructions and a link to a yupiter notebook tutorial. The code is well documented. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors state the data set used in section 5.2 and their source with a link in the citation. There are no descriptions or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameters is appendix D. They are summarised in table 4. The authors conducted a search and define the evaluation strategy but do not specify the budget or strategy.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The data split is defined in apendix D. The authors report average test accuracy and 95% CI over 100 randomly generated data splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on geometric deep learning / GNN and rewiring graphs.
