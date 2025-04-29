
## Asymmetric Action Abstractions for Planning in Real-Time Strategy Games
Rubens O. Moraes, Mario A. Nascimento, Levi H.S. Lelis
Keywords: 
JAIR/2022/Proceedings/13769 - Asymmetric Action Abstractions for Planning in Real-Time Strategy Games.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors link a code base (not theirs) that 'facilitates our empirical evaluation' (https://github.com/Farama-Foundation/MicroRTS). The implementation has clear installation notes, instructions how to use, and very good comments. Structure is very large and can use some guide. However the implementation of their own algorithms are not present in this implementation, but there are some starting points. Pseudo code given alg 1-5.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use muRTS as environment, describe it in 6.1 and provide code for it in the implementation link. They also state the exact instnaces used in table 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

There are parameters discussed for the algorithms 1-5 but they are not discussed in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure winning rate of 100 matches (10 matches per map, 10 maps), number of cycles in table 2. The authors vary the set size N. They measure the branching factor in table 4, with average and maximum factor over 5 indepdendent runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on game strategies.
