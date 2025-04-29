
## Action-modulated midbrain dopamine activity arises from distributed control policies
Jack Lindsey, Ashok Litwin-Kumar
Keywords: 
NeurIPS/2022/Proceedings/54377 - Action-modulated midbrain dopamine activity arises from distributed control policies.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in footnote 1 (https://github.com/jlindsey15/ActionDopamineDistributedControl). The readme is empty. The code needs more comments. No installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The atuhors use simulated environments (TwoJoint and Maze) which they include in their code with a parameter G. Open-field and TwoJoint are used in the paper. A depicition is given in figure 2 with a description in section 5. The G value is fixed to 10 in the code and not modified. Its not completely clear if its used like this everywhere. The Open-field is not given (unless its maze but thats not clear).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyperparameters in section 4. More details are given in appendix A.5. There they state the grids per parameter / algorithm. Three parameters are only given fixed values. The selected values are not stated. No structured overview. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors report mean and standard deviation over the results. Metrics are environment performance and other specific from the paper defined in the introduction. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise in RL policies.
