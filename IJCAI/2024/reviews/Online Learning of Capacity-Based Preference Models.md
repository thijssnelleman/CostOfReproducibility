
## Online Learning of Capacity-Based Preference Models
Margot Herin, Patrice Perny, Nataliya Sokolovska
Keywords: Uncertainty in AI: UAI: Decision and utility theory, Machine Learning: ML: Learning preferences or rankings, Machine Learning: ML: Online learning
Award: Distinguished Paper Award
IJCAI/2024/Proceedings/0787 - Online Learning of Capacity-Based Preference Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://gitlab.com/margother/OPL). In the readme they provide an overview on their method. They also provide a pdf with supplementary materials. The code contains a decent amount of comments, although some files are a bit undocumented. They also provide a requirements file for installation. The repository could do with some more documentation how to use it, but does serve as a good source of information for re-implementation nonetheless.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors do numerical tests on their method in section five on 'synthetic preference data'. They details how the data is generated and provide a notebook on it in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state two pieces of pseudo code in algorithm 1 and 2, with required parameters gamma, delta and T and for the latter also p. They state the values of these parameters in section five, but not how they were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they use accuracy as a metric and training times, doing 'over 20 simulations' per experiment. The authors state they use a test set of 500 examples. The analysis in figure 1,2,3 use different metrics which are domain/task specific and can be assumed as previous experience.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires previous experience in multicriteria decision making. However, the documentation is very complete regarding the experiments s.t. it serves as a very good starting point, but to fully understand what happens this expertise is required.
