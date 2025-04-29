
## Mitigating Value Hallucination in Dyna-Style Planning via Multistep Predecessor Models
Farzane Aminmansour, Taher Jafferjee, Ehsan Imani, Erin J. Talvitie, Michael Bowling, Martha White
Keywords: 
JAIR/2024/Proceedings/15155 - Mitigating Value Hallucination in Dyna-Style Planning via Multistep Predecessor Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors link the libraries for simulation. Extensive pseudo code is provided. Their own implementation is not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use three benchmark environments and provide a citation on each for the implementation. They are not described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors sample the alpha value randomly from the range of [0,0.5] and averaged the performance over 30 random seeds. They state the selected learning ranges and that they report the best performance for each but its not clear what that selected value is. No other parameters are introduced.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

All curves are averages over 30 runs with standard error. Metric is accumulated reward and episode return (environment). Split not applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise with RL.
