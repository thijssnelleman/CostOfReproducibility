
## Your representations are in the network: composable and parallel adaptation for large scale models
Yonatan Dukler, Alessandro Achille, Hao Yang, Varsha Vivek, Luca Zancato, Benjamin Bowman, Avinash Ravichandran, Charless Fowlkes, Ashwin Swaminathan, Stefano Soatto
Keywords: 
NeurIPS/2023/Proceedings/71283 - Your representations are in the network: composable and parallel adaptation for large scale models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide implementation details in appendix F. No practical details given. Overview in fig 2. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(14/14)

The authors state the datasets used with citations in sec 4. No description statistics or direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the training details in section 4. More details are given in appendix F such as grids used to select HPs. A structured overview is missing and selected values from the grids per experiment are also not fully clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The results are presented over test sets. Data split not clear. The metric is top-1 test error. The authors state they report averages but over what they aggregate is not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise in transfer learning.
