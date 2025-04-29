
## Solving Quantum-Inspired  Perfect Matching Problems via Tutte-Theorem-Based Hybrid Boolean  Constraints
Moshe Y. Vardi, Zhiwei Zhang
Keywords: Constraint Satisfaction and Optimization: CSO: Constraint satisfaction, Constraint Satisfaction and Optimization: CSO: Applications, Constraint Satisfaction and Optimization: CSO: Modeling
IJCAI/2023/Proceedings/0227 - Solving Quantum-Inspired  Perfect Matching Problems via Tutte-Theorem-Based Hybrid Boolean  Constraints.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/zzwonder/PMVC). In the readme they state installation requirements, how to run the code with some examples, where the benchmark data can be found, how to add more methods to their experiment set up, and something about encoding. The code has very few comments. The benchmark data can be found in the zip file, as well as an appendix with extra experiments. The implementation could do with better documentation (mainly comments and file structure such as the zip file confusion with the other files present in the repository). The authors have an explanation on their implementations in 6.2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors provide benchmark datasets in their implementation link. The data sets can be directly linked to the experiment names easily. The authors generate these data sets themselves and provide details on it in section 6.2 on how it was generated including the scripts they used to do it in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Based on algorithm 1 the method seems to be parameter free. This can easily be checked against their implementation. No note on parameter (values) are made in the paper, so a check is required.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state each experiment was repeated 100 times and that they present the median. The metric is running time. No training procedure applicable or data splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise with quantum methods, the problem statements and the SOTA solvers on these problems.
