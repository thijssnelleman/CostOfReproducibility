
## Efficient PAC Learnability of Dynamical Systems Over Multilayer Networks
Zirou Qiu, Abhijin Adiga, Madhav Marathe, S. S. Ravi, Daniel Rosenkrantz, Richard Stearns, Anil Vullikanti
Keywords: 
ICML/2024/Proceedings/35107 - Efficient PAC Learnability of Dynamical Systems Over Multilayer Networks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/bridgelessqiu/Learning-Multilayer-Dynamical-Systems-ICML24). In the readme they state the directory structure, how to run the code with examples. There are no installation instructions. The code has a good amount of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

There are alot of datasets available in the implementation. The datasets are presented with statistics in table 1 and citations provided in section 5. Descriptions on the datasets are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors evaluate variable p on a grid. There is no clear summary on the parameters of their method, neither in the implementation. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the present the results where each data point is averaged over 50 experiments. They also state the std dev of each point is less than 0.08/0.09. The metric used is empirical loss. The authors present the results over a varying training set size.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on multilayer dynamical systems optimisation.
