## Cooperatively Coevolving particle swarm optimization for large scale optimization
Xiaodong Li, Xin Yao
Keywords: Cooperative coevolution, evolutionary algorithms, large-scale optimization, particle swarm optimization, swarm intelligence
extra_reviews/2012/Proceedings/Cooperatively Coevolving particle swarm optimization for large scale optimization.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation. Detailed pseudo code in algorithm 1 and 2. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use seven benchmark functions from CEC’08 and provide a citation. They add four extra functions, rotated versions of four of the seven benchmarks. The authors do not provide their implementation, so the generators will have to be redone based on the documentation (See citation, quite extensive there).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors describe the algorithm parameters in pseudo code 1/2. The authors state the grids of parameter S values in sec V.A. The authors specify that one parameter s was replaced by an adaptive scheme in their solution, but also evaluate it on a grid.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure the function value, and present the averages with standard error over 25/50 independent runs. Split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
