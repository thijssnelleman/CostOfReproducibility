
## Approximate Counting of Linear Extensions in Practice
Topi Talvitie, Mikko Koivisto
Keywords: 
JAIR/2024/Proceedings/16374 - Approximate Counting of Linear Extensions in Practice.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors link their implementation in the introduction (https://github.com/ttalvitie/linext). In the readme they state the method and an index on the directories. They state how to compile, and what is needed for the compilation. There is an overview of the arguments of the code, what the results will look like, which algorithms are supported, and licenses. Code has very few comments. The amount of code files is huge and could use its own index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors generate two datasets in 6.2 and describe / cite the process and provide the parameter values. Code is available in the implementation. Statistics on the generated data is available in table 2 and the datasets are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the parameter values of the algorithms in 3.4/4.4, stating 'we observed these values to perform well on average' and 'in preliminary experiments', indicating empirical/human optimisation but budget is not stated for acquisition. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results with median and range over 5 independent instances per n value over running times. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on approximate counting problems.
