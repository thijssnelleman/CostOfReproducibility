
## A Top-Down Tree Model Counter for Quantified Boolean Formulas
Florent Capelli, Jean-Marie Lagniez, Andreas Plank, Martina Seidl
Keywords: Constraint Satisfaction and Optimization: CSO: Satisfiabilty, Constraint Satisfaction and Optimization: CSO: Solvers and tools
IJCAI/2024/Proceedings/0205 - A Top-Down Tree Model Counter for Quantified Boolean Formulas.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present their implementation link (https://zenodo.org/records/11153123). In the readme they explain what each file in the repository contains. In the readme of the code they explain how to compile/use it with example output. The code is well documented with comments. They also provide logs for all the experiments presented in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(7/7)

The authors include the benchmarks used in their implementation documentation. The authors discuss the used benchmarks in detail in section 4 and provide citations on their sources, and they also include statistical properties of the data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The presented method is parameter free (based on algorithm 1 and the implementation).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate their method on the benchmark data sets.They measure the runtime of their method and the target output (tree model count) of the task. They state the quantifier alternations n used for their experiments for 'crafted instances' benchmarks.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires an understanding of SAT solving and the specific problem presented.
