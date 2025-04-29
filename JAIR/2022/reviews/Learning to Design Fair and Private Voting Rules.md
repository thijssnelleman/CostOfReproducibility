
## Learning to Design Fair and Private Voting Rules
Farhad Mohsin, Ao Liu, Pin-Yu Chen, Francesca Rossi, Lirong Xia
Keywords: 
JAIR/2022/Proceedings/13734 - Learning to Design Fair and Private Voting Rules.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given. Comparison overview in figure 1, structure in figure 2. Pseudo code in algorithm 1-3.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The author use synthetic datasets, describe the models used for generation in section 8, and the procedure. Implementation not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors use XGBoost as underlying/input model but do not specify the parameters. They also state a β parameter for weighting but these are not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The auhtors measure concordet efficiency (defined in 3.2.) versus average fairness and average rank utilty (5.1). The avearge function is defined in section 8. The results are aggregated over the data set (population).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on fairness in Ai and voting.
