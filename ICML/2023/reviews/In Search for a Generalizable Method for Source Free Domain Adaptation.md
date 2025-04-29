
## In Search for a Generalizable Method for Source Free Domain Adaptation
Malik Boudiaf, tom denton, Bart van Merrienboer, Vincent Dumoulin, Eleni Triantafillou
Keywords: 
ICML/2023/Proceedings/23939 - In Search for a Generalizable Method for Source Free Domain Adaptation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/7)

The authors describe the datasets in appendix A with a citation, descriptions and statistics. Four are public three are 'unreleased' but 'work is underway to open-source'.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the parameter grids used in table 8, summarising the hyperparameters and their possible values for each experiment. They state for each experiment optimisation was conducted on the validation set. The optimisation technique is grid search.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the data split in appendix A (75-25) and a seperate data set for validation. The authors use mean average precision as metrics. The authors present the results averaged over 5 random seeds. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in source free domain adaptation. Due to the implementation not published practical experience is needed as well.
