
## Backprop-Free Reinforcement Learning with Active Neural Generative Coding
Alexander G. Ororbia, Ankur Mali
Keywords: Cognitive Modeling & Cognitive Systems (CMS), Machine Learning (ML)
AAAI/2022/Proceedings/19876 - Backprop-Free Reinforcement Learning with Active Neural Generative Coding.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation. They provide a general process flow of the method, an architecture design, and a detailed pseudo code on their method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(4/4)

The authors use four common RL environments for their experiments, but citations are not provided. They state details related to these environments are provided in the appendix but this is missing (AAAI limitations). The text implies these environments are public ('commonly used') but its not clear which implementation they have used.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

They refer to the appendix which is missing (AAAI limitations) for the meta parameters. They state they choose the values based on preliminary experimentation ('human optimisation'). Some values are provided in the paper regarding the parameters required in the pseudo code but not all values seem to be presented.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present their results with mean and standard deviation over the episodic reward with 10 trials per experiment/method. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise in RL and backpropagation/backprop-free concepts.