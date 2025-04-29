
## QCDCL with Cube Learning or Pure Literal Elimination - What is Best?
Benjamin Böhm, Tomáš Peitl, Olaf Beyersdorff
Keywords: Constraint Satisfaction and Optimization: Satisfiabilty, Constraint Satisfaction and Optimization: Solvers and Tools
Award: Distinguished Paper
IJCAI/2022/Proceedings/0248 - QCDCL with Cube Learning or Pure Literal Elimination - What is Best?.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors study other methods and analyse them to advice how they should best be implemented. The atuhors provide no link to these implementations used for their experiment, rather they cite the works they used. These can be considered as baselines and thus the reproduction of the experiments' implementation is a re-implementation of the methods used, not this work.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use a data set which they name in section 8 and provide a direct link to. They also state the method was run on 'each of the formulas used for separations in this paper', which will take some field expertise to extract which ones these actually are (but are thus presented publicly). There is very little description on the data in section 8. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors explore various parameter settings of the used method in figure 2 to explore the iumpact of the parameter values and heuristics on the method. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate 24 configurations of the used method on the full dataset and evaluate it over running time, but the 'n' variable on the x-axis takes some domain knowledge to follow. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries alot of expertise on the problem presented to understand the theorems and proofs, as well as grasp the experiment in section 8.
