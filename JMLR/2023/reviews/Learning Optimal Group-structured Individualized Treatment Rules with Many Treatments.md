
## Learning Optimal Group-structured Individualized Treatment Rules with Many Treatments
Haixu Ma, Donglin Zeng, Yufeng Liu
Keywords: 
JMLR/2023/Proceedings/220520 - Learning Optimal Group-structured Individualized Treatment Rules with Many Treatments.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide pseudo code in appendix E. No other implementation details.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors conduct experiments on simulated data. The setting per experiment is given in section 4 with parameters. No implementation. In section 5 they use STAR*D and provide a citation. Description is given no direct link or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

There are notes on tuning parameters in 2.2 named λ which is in section 4 chosen by 10 fold cross-validation from a grid. Selected value not given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors report square root of MSE as well as ratio and misclassification rate (aggregation implied). Results are on independent test data. How the split was done is not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on group structure.
