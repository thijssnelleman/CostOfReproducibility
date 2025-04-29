
## The Secretary Problem with Predicted Additive Gap
Alexander Braun, Sherry Sarkar
Keywords: 
NeurIPS/2024/Proceedings/95582 - The Secretary Problem with Predicted Additive Gap.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state experiments were conducted in Python 3.9. Pseudo code is provided in algortihm 1-3. The authors state in the checklist the code should be easily re-implementable. Although the method does seem relatively 'short', more practical details regarding the implementation are needed to make this 'easy'.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors use a simulated problem and describe it in 6.1.1. in details. The authors state how many iteration they run it for and n is specified. The implementation is not given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The algorithm parameters are stated in 6.1.1. and in figure 3 various parameter values are done vore the adaptive gap. No acquisition applicable. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Experimental setup is stated in 6.2.1 with parameter values. Runs are averaged over 5000 iterations per class. Split not applicable. metric is competitive ratio (problem metric). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on the secratary problem and information weakness.
