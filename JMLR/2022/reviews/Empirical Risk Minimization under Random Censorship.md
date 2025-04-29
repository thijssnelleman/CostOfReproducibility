
## Empirical Risk Minimization under Random Censorship
Guillaume Ausset, Stephan Clémençon, François Portier
Keywords: 
JMLR/2022/Proceedings/19450 - Empirical Risk Minimization under Random Censorship.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state a link to their implementation in section 4 (https://github.com/aussetg/ipcw). The repository is empty.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(2/2)

The authors use synthetic data for their experiments, describe the models with citations and the parameters with the values. Implementation not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors make various statements about the hyperparameters, but do not state what these actually are. They also refer to 'default values' in packages. Very little information provided.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors define prediction error as a metric. Figure 1 shows result over n training samples and figure 2 with various values of p with n = 1000 but the variation / aggregation, population is over 100 repitions. Data split is explained but its not clear on which set they present the results. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on censored data and risk minimization.
