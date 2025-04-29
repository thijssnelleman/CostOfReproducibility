
## Generalizing Group Fairness in Machine Learning via Utilities
Jack Blandin, Ian A. Kash
Keywords: 
JAIR/2023/Proceedings/14238 - Generalizing Group Fairness in Machine Learning via Utilities.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state a link to their implementation in footnote 7 (https://github.com/jackblandin/group-fairness-in-machine-learning-via-utilities). In the readme they state how to install and how to reproduce the experiments briefly. Code needs more comments. Structure is large and can use an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use the loan apllication scenario from the German Credit Dataset and provide a citation, describe it but provide few statistics. The data is available in the implementation. The authors also use the 2020 US Census dataset (citation given, description given, dataset not found).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

There are some notes to be found regarding algorithm parameters in the code, but there are no notes on it in the paper.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure 'cost' (eq 5.1.) and 'fairness' with three ratios (DemParClfRatio, EqOppClfRatio and DemParUtilRatio) which are defined in eq 5.2-5.4. The measurements are done over 10-fold cross validation and report average 10/90th percentiles. For the census dataset the authors present clustering results over well-balancedness (formula given) and τ.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on fairness.
