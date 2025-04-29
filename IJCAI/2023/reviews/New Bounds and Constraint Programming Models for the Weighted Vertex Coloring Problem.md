
## New Bounds and Constraint Programming Models for the Weighted Vertex Coloring Problem
Olivier Goudet, Cyril Grelier, David Lesaint
Keywords: Constraint Satisfaction and Optimization: CSO: Constraint programming, Search: S: Combinatorial search and optimisation
IJCAI/2023/Proceedings/0214 - New Bounds and Constraint Programming Models for the Weighted Vertex Coloring Problem.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/Cyril-Grelier/gc_wvcp_cp). In the readme they state installation/compilation instructions, how to download the data sets directly through the implementation, an overview of the file/directory structure which is large but well explained. The source code has a seperate readme. The code is well commented.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors state the data used in the introduction of section 5, with citations and details, and refer for further information to the supplementary material. The implementation directly links the data sets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Based on algorithm 1, and the implementation, there are certain parameters that should be passed but these are rather problem/solution parameters (semantic) than performance parameters. These parameters are explored in table 1, 2 and 3. They are problem/instance dependant, so no acquisition applicable.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate their method on the presented data set in single runs, the stated values are problem specific metrics which they explain in the problem statement. They also measure running time in seconds for table 1 and 3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires an understanding of the problem/SOTA, but the documentation is very complete making it very well self contained.