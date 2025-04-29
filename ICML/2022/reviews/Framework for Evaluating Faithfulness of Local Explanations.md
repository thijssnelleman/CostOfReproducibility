
## Framework for Evaluating Faithfulness of Local Explanations
Sanjoy Dasgupta, Nave Frost, Michal Moshkovitz
Keywords: 
ICML/2022/Proceedings/17445 - Framework for Evaluating Faithfulness of Local Explanations.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. Pseudo code given in appendix C.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(7/7)

The authors describe 7 datasets with statistics in appendix D, descrtiptions with citations for most and direct links for some are in section 5.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the HP values in appendix D.2. and table 4 gives a full overview. The authors specify the search grids in D.2. as well (budget implied). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors split the data sets 66% for training and cross-validation (Appendix D.2.), they select the best values on 3 repititions mean. The presented final results are over 5 repitions with an average plus CI of 95%. table 1 has mean and standard dev. The used metrics are explained in detail with formulas in section 3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on local explanations and faithfulness.
