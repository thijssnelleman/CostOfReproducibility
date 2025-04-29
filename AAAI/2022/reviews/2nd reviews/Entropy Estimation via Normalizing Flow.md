## Entropy Estimation via Normalizing Flow
Ziqiao Ao, Jinglai  Li
Keywords: Reasoning Under Uncertainty (RU)
AAAI/2022/Proceedings/21237 - Entropy Estimation via Normalizing Flow.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

no implementation: +4 
framework not given: +4
no pseudo-code nor figures illustrating implementation: +2

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

Code for generating the synthetic data is not provided: +5
I think the parameters and how the data is generated is provided: +0

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

Their method uses e.g. knn but I can not see the value of k. I don't think they give any hyperparameter configuration and how it was obtained.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

rmse is clear, 
data used for evaluation is clear as well (sampled from distributions),
strategy is there -> 100 trials
aggregation should be clear.


### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

I think it is implementation wise not super difficult, but one needs to be sure that everything is correctly put together. Given only the formulas I imagine that to be difficult.