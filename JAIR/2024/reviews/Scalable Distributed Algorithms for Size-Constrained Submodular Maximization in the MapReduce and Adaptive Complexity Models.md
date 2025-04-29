
## Scalable Distributed Algorithms for Size-Constrained Submodular Maximization in the MapReduce and Adaptive Complexity Models
Yixin Chen, Tonmoy Dey, Alan Kuhnle
Keywords: 
JAIR/2024/Proceedings/15484 - Scalable Distributed Algorithms for Size-Constrained Submodular Maximization in the MapReduce and Adaptive Complexity Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors provide a set of instructions for installation of the implementation in appendix G but the link for the repository that you're supposed to clone in step 5 is not given. Extensive pseudo code provided in detail.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/4)

The authors state the dataset size in table 2. In appendix F they state the details on each task, and the data seems to be generated for task 1 (few details, no code) for task 2 they use CIFAR-10 (few details, only a citation) for task 3 they use Youtube online social network data (only cited) and the Youtube dataset (cited).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Input parameters are stated in the pseudo code of the algorithms but they all seem to be regarding to the input.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure the runtime in seconds and the objective function over k. Timeout of each algorithm was set to 6 hours.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on distributed computing.
