
## Adaptive Greedy versus Non-adaptive Greedy for Influence Maximization
Wei Chen, Binghui Peng, Grant Schoenebeck, Biaoshuai Tao
Keywords: 
JAIR/2022/Proceedings/12997 - Adaptive Greedy versus Non-adaptive Greedy for Influence Maximization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors state statistics on the dataset in table 2 (Nethept, CA-HepPh, DBLP and com-YouTube). The authors provide a link to the SNAP datasets in the references, where they state in 7.2 that all the datasets are sourced from here. Descriptions are lacking. The authors also do synthetic data in 7.4, and provide the construction process in 3.1. and parameter values are provided but implementation is not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state two parameter ε,δ and analyise them theoretically and provide formulae for their settings.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the number of infected vertices over number of seeds (defined in 2.1.). The authors also show in table 3/4 various numbers of MC simulations / varying k, measuring the greedy adaptivity gap but the exact metric definition is not clear. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on greedy algorithms and adaptive influence maximization problem.
