
## Consistent Adversarially Robust Linear Classification: Non-Parametric Setting
Elvis Dohmatob
Keywords: 
ICML/2024/Proceedings/34236 - Consistent Adversarially Robust Linear Classification: Non-Parametric Setting.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation for the empirical validation of section 6.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/2)

The authors conduct experiments on distributions (synthetic) which they provide in great details with citations. Implementations missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors define a bandwidth parameter and specify it over a formula in section 6. Acquistion not applicable (Seems to be a semantic parameter?). The epsilon parameter is evaluated over a grid.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors specify the sample sizes for the experiments and the authors measure adversarial regret as a metric. The metric is defined in equation 5. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires experience with adversarial attacks, computational complexity, linear classification and theoretical knowledge as well.
