
## Safe Reinforcement Learning via Probabilistic Logic Shields
Wen-Chi Yang, Giuseppe Marra, Gavin Rens, Luc De Raedt
Keywords: Uncertainty in AI: UAI: Statistical relational AI, Knowledge Representation and Reasoning: KRR: Learning and reasoning, Machine Learning: ML: Reinforcement learning
Award: Distinguished Paper
IJCAI/2023/Proceedings/0637 - Safe Reinforcement Learning via Probabilistic Logic Shields.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The implementation of the method can be found online (https://github.com/wenchiyang/pls). In the readme they state the dependencies and how they can be installed, how to run an example including full files,  how to evaluate, how to configure the method, and some environment details. The code has a lot of comments, the structure is not too large. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use simulated environments which they provide online in their implementation. The environments are explained in the experimental setup. The authors state two configurations are used per environment in appendix A.3. They are detailed in table 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors do a hyperparameter search using grid search and specify the values. The best found values are selected for the rest of the experiments. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they evaluate on two metrics which they explain and refer to appendix for details. They conduct four experiments for their four questions and explain them in great details. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in RL, and although the documentation is very complete (including the implementation), to understand the method and the experiments conducted a lot of expertise or various stepping stone sources are needed beforehand.
