
## Joint Optimization of Concave Scalarized Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm
Qinbo Bai, Mridul Agarwal, Vaneet Aggarwal
Keywords: 
JAIR/2022/Proceedings/13981 - Joint Optimization of Concave Scalarized Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state in 6.2. they use PyTorch 1.0.1. as their framework. Implementation not given. Pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors define the simulation environment in 6.1. Implementation is not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state various hyperparameter values and choices in 6.2. They also provide the values of their method in 6.1. Acquisition not given and no structured overview. Some parameters are varied over the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the result over 10 independent iterations and plot the mean +/- std dev in the figures. the authors measure fairness utility with alpha=2 as defined in eq. 3. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on MO RL.
