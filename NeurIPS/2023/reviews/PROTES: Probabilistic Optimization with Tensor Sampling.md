
## PROTES: Probabilistic Optimization with Tensor Sampling
Anastasiia Batsheva, Andrei Chertkov, Gleb Ryzhakov, Ivan Oseledets
Keywords: 
NeurIPS/2023/Proceedings/71674 - PROTES: Probabilistic Optimization with Tensor Sampling.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/anabatsh/PROTES). In the readme they state the method briefly, provide installation instructions, how to use the method, the parameters with lengthy explanations, some notes on the code, list of authors. There is also a document on the workflow regarding installation. The code can use some more comments in the protes directory (main code). Structure is easy. Schematic of the method is given in figure 1. Pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors present results on 4 problem types. They state the problems used in each type in section 6.1-6.4. For the parameters of some of the problems they refer to previous works. Citations are not given for each. For some the problem formulas are given. The code is given for each problem in PROTES/calc/calc.py with parameter values. Statistics not applicable. The general setup of each problem is described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the parameter values in section 6. They map to those presented in algorithm 1. They also describe them in appendix A3 where they present a grid search over various problems with various HP values. A structured overview of the values and the search is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method on each benchmark as minimzation results. There is no metric, the target is to approximate the minimum value of each model. Results are single run. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on optimization of blackbox functions. 
