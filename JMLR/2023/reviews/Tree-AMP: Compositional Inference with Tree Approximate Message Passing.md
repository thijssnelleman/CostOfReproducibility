
## Tree-AMP: Compositional Inference with Tree Approximate Message Passing
Antoine Baker, Florent Krzakala, Benjamin Aubin, Lenka Zdeborová
Keywords: 
JMLR/2023/Proceedings/20695 - Tree-AMP: Compositional Inference with Tree Approximate Message Passing.pdf
Project URL: https://github.com/sphinxteam/tramp

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to the implementation in the abstract and the JMLR website (https://sphinxteam.github.io/tramp.docs/0.1/html/index.html). In the readme thety state installation requirements and link examples. The code has a seperate documentation website with examples and code details. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors conduct experiments on simulated data in 4.1, in 4.2 use MNIST but provide little details on the dataset and in 4.3 on anohter synthetic exmperiment. The implementation of the simulation is given in their package. The values can be found on the linked gallery. Acquisition not specified.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the parameters number of iterations in each pseudo code. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate single runs, evaluate MSE.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on state evolution.
