
## Lifting (D)QBF Preprocessing and Solving Techniques to (D)SSAT
Che Cheng, Jie-Hong R. Jiang
Keywords: CSO: Solvers and Tools, CSO: Constraint Optimization, CSO: Constraint Satisfaction, CSO: Other Foundations of Constraint Satisfaction & Optimization, CSO: Satisfiability
AAAI/2023/Proceedings/25504 - Lifting (D)QBF Preprocessing and Solving Techniques to (D)SSAT.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/NTU-ALComLab/DSSATpre) with an explanation on its design and framework. Build instructions are provided, and how to run the program with examples. The code base is rather large and could do with an architectural schematic. The code is extremely well commented. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors provide a source for their 2 benchmarks (https://github.com/jurajsic/DQBFbenchmarks). Descriptions and statistics are provided, sources are cited.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state in their work that optimal configuration may vary from solver to solver and that theirs performs roughly the same with all configurations. However their implementation documentation seemingly shows there are a lot more configurable parameters to their method. It will take some effort to fully understand the configuration space of this method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The experimental procedure is clearly stated and straightforward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a deep understanding of SAT solving and being up-to-date with SOTA.
