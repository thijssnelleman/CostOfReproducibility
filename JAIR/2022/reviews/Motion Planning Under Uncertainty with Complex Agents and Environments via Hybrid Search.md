
## Motion Planning Under Uncertainty with Complex Agents and Environments via Hybrid Search
Daniel Strawser, Brian Williams
Keywords: 
JAIR/2022/Proceedings/13361 - Motion Planning Under Uncertainty with Complex Agents and Environments via Hybrid Search.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state in 10.1 the algorithms were implemented in C++ and used CUDA for GPU parallelization. They also state they used SNOPT 7.6 as optimizer with citation. Implementation is not shared.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(0/4)

The authors details several assumptions and details regarding the environment in 3.2. They use four sets of test cases in section 10. Each is described and visualised but no implementation is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

Not discussed.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure time in ms and objective value for task 1, search times on 5 test cases (ms) with a timeout at 5 min for task 2 and the value function in table 2, chance of constraint error and evaluation time for task 3 and 4. Objective functions defined per task.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on hybrid search.
