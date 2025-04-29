
## LESSON: Learning to Integrate Exploration Strategies for Reinforcement Learning via an Option Framework
WOOJUN KIM, Jeonghye Kim, Youngchul Sung
Keywords: 
ICML/2023/Proceedings/24279 - LESSON: Learning to Integrate Exploration Strategies for Reinforcement Learning via an Option Framework.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/beanie00/LESSON). In the readme they show a figure of the architecture, instalation instructions, how to run the training procedure with an explanation on the arguments and an example and an ackownledgement for another repository regarding part of the implementation. The code has very few comments. The repository structure is small enough to oversee. Psuedo code is available in algoriythm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two environments for their experiments and provide citations on them, with parameter values and descriptions in appendix A.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors list the hyperparameter values in appendix B per experiment (table 1a). The presented parameters were tuned over a grid. In the paragraph above the table more parameters are listed but no acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors present the results averaged over 10 random seeds for 1 environment and 3 for another. It is not clearly stated what the 'performance' metric is nor the variation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on reinforcement learning.
