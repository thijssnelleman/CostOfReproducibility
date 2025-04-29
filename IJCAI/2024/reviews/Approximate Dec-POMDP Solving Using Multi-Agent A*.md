
## Approximate Dec-POMDP Solving Using Multi-Agent A*
Wietze Koops, Sebastian Junges, Nils Jansen
Keywords: Planning and Scheduling: PS: Planning under uncertainty, Agent-based and Multi-agent Systems: MAS: Multi-agent planning, Planning and Scheduling: PS: POMDPs
IJCAI/2024/Proceedings/0745 - Approximate Dec-POMDP Solving Using Multi-Agent A*.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link with supplementary material (https://zenodo.org/records/11160648) which contains their implementation. Large parts of the code are well documented with comments. The readme contains details on the directory and file structure, as well as how to execute the code for the benchmarks. There are some notes on the implementation in section 7, including details on how it was executed on the target system.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(9/9)

The authors state they use standard benchmarks and provide a citations on each and for two the parameters used. No descriptions are given on the tasks so this is required expertise. Five datasets are present in the implementation. As there is little documentation given on the data, there is some effort required here to check that where the data is available and what the tasks are to defend comparability if using a different dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state their hyperparameter selection in section 7. They state limits on their search space for 2 parameters, and fixed values for three others. The used values of the remaining hyperparameters are found in table 1 and they show the results of the various combinations in table 2 and 3. Although this is not explicitly stated, this is grid search. They also state these values for each benchmark in the scripts in their implementation. The name hyperparameter here is a bit confusing as there are seemingly no 'parameters' in the method: Rather this is algorithm configuration.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the maximum time for eachmethod in the setup paragraph of section 7. No training procedure used. The results are single runs. The authors show how to re-run the benchmarks in their implementation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires a good understanding of AI planning.
