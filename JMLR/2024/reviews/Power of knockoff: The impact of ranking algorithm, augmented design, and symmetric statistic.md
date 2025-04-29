
## Power of knockoff: The impact of ranking algorithm, augmented design, and symmetric statistic
Zheng Tracy Ke, Jun S. Liu, Yucong Ma
Keywords: 
JMLR/2024/Proceedings/211137 - Power of knockoff: The impact of ranking algorithm, augmented design, and symmetric statistic.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

No implementation provided.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(4/4)

The authors do simulations in section 8, and state the problems with parameters per experiment. No implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Lasso-path and least-squares are tuning free (section 2). They also motivate what has to happen to a tunable parameter λ. However in the evaluation all methods used are among the aforementioned tuning free types.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure 200 generated datasets and record the averaged hamming selection error. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on hknockoff rates and rare/weak signal models.
