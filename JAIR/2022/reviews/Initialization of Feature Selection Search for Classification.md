
## Initialization of Feature Selection Search for Classification
Maria Luque-Rodriguez, Jose Molina-Baena, Alfonso Jimenez-Vilchez, Antonio Arauzo-Azofra
Keywords: 
JAIR/2022/Proceedings/14015 - Initialization of Feature Selection Search for Classification.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given, pseudo code in alg 1-6.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(26/27)

The authors take datasets from UCI, OPENML and a artificially generated dataset Parity3+3. They select 27 datasets in total and list details on each in table 2. Links and descriptions missing. It is unclear where Parity3+3 exactly comes from.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the best parameter and measure for each method in table 3, and state that they considered in total 30 options, and obtained this they used 3 independent datasets (appendicitis, lung cancer and horse-colic) and selected each based on the calssification accuracy in the average ranking among these datasets.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics with a description in 5.1. The authors use 10-fold stratified cross validation and present the mean and standard deviation over it. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on feature selection.
