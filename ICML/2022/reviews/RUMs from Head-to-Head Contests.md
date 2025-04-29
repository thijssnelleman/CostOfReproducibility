
## RUMs from Head-to-Head Contests
Matteo Almanza, Flavio Chierichetti, Ravi Kumar, Alessandro Panconesi, Andrew Tomkins
Keywords: 
ICML/2022/Proceedings/16895 - RUMs from Head-to-Head Contests.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state they implemented their method in Python using IBM cplex 'as the LP solver'. Pseudo code is provided in algorithm 1, 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

They use 7 different datasets for which they provide citations and a birefy descritpions in 6.2. but real details are missing. No direct links provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state in the introduction their method contains no hyper-parameters to tune.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate average error. The results are presented as the average over 20 runs. They also report RMSE in a cross validation experiment by 5-fold cross validation repeated 10 times. They report the std dev are within a certain range. A few details regarding aggregations/variation are a bit unclear but in general all information is there.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on random utility models.
