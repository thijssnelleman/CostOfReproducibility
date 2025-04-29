
## Inverting Cryptographic Hash Functions via Cube-and-Conquer
Oleg Zaikin
Keywords: 
JAIR/2024/Proceedings/15244 - Inverting Cryptographic Hash Functions via Cube-and-Conquer.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors prove two implementation links one in footnote 3 (https://github.com/olegzaikin/EnCnC) and one in the references (https://zenodo.org/records/13766981). Code has okay comments. There are make files included, but its not given under what circumstances it must be compiled (what compiler etc).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors construct a dataset and provide a it online. They state the procedure in 5.4, and provide charatecirstics on it in table 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the values of the parameters in 6.2 and reason the values, some were 'chosen in preliminary experiments'. Only the budget is not clear under which they were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Authors measure runtime over number of simplification conflicts. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on has functions and SAT solving.
