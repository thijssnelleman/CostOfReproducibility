
## A Rigorous Risk-aware Linear Approach to Extended Markov Ratio Decision Processes with Embedded Learning
Alexander Zadorojniy, Takayuki Osogami, Orit Davidovich
Keywords: Planning and Scheduling: PS: Markov decisions processes, Machine Learning: ML: Reinforcement learning, Uncertainty in AI: UAI: Sequential decision making
IJCAI/2023/Proceedings/0608 - A Rigorous Risk-aware Linear Approach to Extended Markov Ratio Decision Processes with Embedded Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present an algorithm to find the optimal policy for EMRDP with theoreticaly gaurantees, which they evaluate empirically. The algorithm is presented as pseudo code in algorithm 3. They present they implementation online and link it (https://github.com/IBM/IBM-Extended-Markov-Ratio-Decision-Process). The readme contains information on the environment, how to work with the configurations, how to install, where to find the parameters of the enviornment, and how to execute the code. There are many other details regarding the environment and how to work with it. and even some details on common issues and how to fix. The notebooks are really well documented. The code has plenty of detailed comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a benchmark grid world problem, which they include in their implementation docs including the parameters under which the environment was run.  They show an example of it in figure 3. A full notebook is dedicated to its usage in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors discuss several values regarding their theoretically optimal policy in 7.1/7.2 regarding the environment setup, which can easily be checked against the values in their emrdp.yaml/config.json files. They mainly refer to previous works for their selection. These values are directly fed into the algorithm.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state how the environment was sampled for every experiment. They provide the mean confidence interval in their results. They present algorithm optimal ratio over theoretical optimal ratio as metric which they explain in 7.2. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise with Markov processes.
