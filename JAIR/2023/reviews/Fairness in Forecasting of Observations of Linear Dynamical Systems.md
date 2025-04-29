
## Fairness in Forecasting of Observations of Linear Dynamical Systems
Quan Zhou, Jakub Mareček, Robert Shorten
Keywords: 
JAIR/2023/Proceedings/14050 - Fairness in Forecasting of Observations of Linear Dynamical Systems.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state a link to the implementation in section 4 (https://github.com/Quan-Zhou/Fairness-in-Learning-of-LDS). In the readme they state installation dependencies and an index of the code files. Code can use better comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use the COMPAS dataset and provide a direct link to it in the implementation and describe in in the introduction. No statistics. The authors also state the procedure on generating biased data in 4.1. and code is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors use a delta 1 and 2 parameter, one is varied and the other is fixed to 0.01. Acquisition for the second not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors define the nrmse metric in 4.3. and results are presented over 10 experiments and shown with mean and standard deviation, in figure 3 with quartiles. In figure 3 the metric is runtime in seconds and presented with mean and standard deviation over three runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on linear dynamical systems and fairness.
