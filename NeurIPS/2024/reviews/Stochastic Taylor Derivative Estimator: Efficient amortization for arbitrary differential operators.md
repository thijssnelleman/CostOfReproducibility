
## Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators
Zekun Shi, Zheyuan Hu, Min Lin, Kenji Kawaguchi
Keywords: 
Award: Best Paper
NeurIPS/2024/Proceedings/1535 - Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/sail-sg/stde). In the readme they state how to install, how to run examples with parameter value explanation and how to reproduce the exact results as shown in the paper. The config.py and types.py are well commented but the other seem to be a bit lacking. Structure is easy/small.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use PDE formulas (real world?) which they provide in the implementation. The parameters of this data is given in sec 5. A descriptions on the data is not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors summarise the architecture and HP values in appendix H. Acquisitition is not specified. Parameter values used for each experiment also given in implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors run each experiment five times with random seeds and report average + std dev. The authors evaluate the method on speed and memory reduction in table 1 and 2 in iterations per second and MB. They vary the experiment over amount of dimensions in the problem.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

Requires expertise in  stoachtistic gradient descent, taylor derivative estimation and practical implications of the algorithms regarding reducing runtime and memory usage.
