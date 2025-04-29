
## Sparse GCA and Thresholded Gradient Descent
Sheng Gao, Zongming Ma
Keywords: 
JMLR/2023/Proceedings/210745 - Sparse GCA and Thresholded Gradient Descent.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors use simulated datasets and define each with formulas and parameters in 5.1, and 5.3. Some simulation settings are referred to a previous work but are given. Implementation not present.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the parameters in 5.2. They fix some with values and others with formulae. An overview of the parameters is given in algorithm 1 as 'Tuning Parameters'. The values are given per experiment. No acquisition specified except for the grid of parameter λ in 5.2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Each experiment is repeated 50 times in 5.1 and they report median error with absolute deviations. In 5.2. they conduct five fold cross validation and state how this was conducted, reporting the result with averages and error bars of one standard deviation on the test data and the metric calculation is defined in the formula on page 16. In table 7 they report the median error over 100 repitiions. Metric is estimation error. Test set is the holdout set in each fold (1/5th).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on sparse GCA.
