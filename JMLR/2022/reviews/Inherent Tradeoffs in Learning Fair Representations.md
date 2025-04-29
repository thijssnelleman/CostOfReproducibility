
## Inherent Tradeoffs in Learning Fair Representations
Han Zhao, Geoffrey J. Gordon
Keywords: 
JMLR/2022/Proceedings/211427 - Inherent Tradeoffs in Learning Fair Representations.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use the adult dataset in section 7 and provide a description with statistics but no citation or link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors specify fixed architectures in section 7. The authors state hte learning rate, optimiser, training apochs and batch sizes are all the same but do not state what these are. The p coeficient is varied on grid for which they show all results. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state a static t/t split in section 7. The metric is joint error across groups and accuracy parity (citation + definition 3). Results are single run, but it is not stated on which dataset the results are.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires experience with fair representations / fairness in algorithms.
