
## Threshold Treewidth and Hypertree Width
Robert Ganian, Andre Schidler, Manuel Sorge, Stefan Szeider
Keywords: 
JAIR/2022/Proceedings/13661 - Threshold Treewidth and Hypertree Width.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide two links in footnote 9 for their implementation (https://github.com/ASchidler/htdsmt/tree/weighted) (https://github.com/ASchidler/tw-sv). Code needs better comments. There is an environment.yml for installation in one of the repos.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use two benchmark datasets twlib and hyperbench, and provide direct libks to them in footnote 11 and 12. Descriptions/details lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the different configurations of the algorithms they use in table 1 and evaluate them.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors run the experiments with 8gb memory limit and 2 hour time limits. The labels on the graphs are not always clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise in CSP/SAT solving and treewidth/hypertree.
