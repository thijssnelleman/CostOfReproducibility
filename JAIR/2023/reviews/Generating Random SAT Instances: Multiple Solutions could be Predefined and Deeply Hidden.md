
## Generating Random SAT Instances: Multiple Solutions could be Predefined and Deeply Hidden
Dongdong Zhao, Lei Liao, Wenjian Luo, Jianwen Xiang, Hao Jiang, Xiaoyi Hu
Keywords: 
JAIR/2023/Proceedings/13909 - Generating Random SAT Instances: Multiple Solutions could be Predefined and Deeply Hidden.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors generate instances for SAT. The algorithm is well explained, and in 5.1 they give details on how it is applied with parameter values for the experiments. The generated data nor the generator is given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors define a parameter K and r in algorithm 2, and the authors vary the value of r in their experiments but K is fixed to 3 and not explained why.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure runtime of other algorithms on their generated data using runtime in seconds. They also evaluate the performances of the solvers when varying the maxH variable over the 'number of flips'. The experiment is repeated 29 times to create the population and they present median and boxplots.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on SAT.
