
## Leaping through Time with Gradient-Based Adaptation for Recommendation
Nuttapong Chairatanakul, Hoang NT, Xin Liu, Tsuyoshi Murata
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20562 - Leaping through Time with Gradient-Based Adaptation for Recommendation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide any details on their implementation. Pseudo code is given for their meta optimisation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The author state they use three publicly available datasets, provide citations on them and a direct link for one. They provide statistics on the datasets, and show a pattern on it over time. A detailed description is given on each data set. The direct link for the other two data sets will have to be determined, which is little effort.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors conduct a hyperparameter and architecture search over a grid. Not every hyperparameter has a grid, such as the optimiser. They provide results on parts of these searches and a sensitivity analysis. It is unclear if it was an exhaustive grid search, but this does seem implied.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

They state how the data was dived in t/v/t, the metrics used for evaluation (without explanation of their meaning, but according to the authors these are commonly used) and based on the descriptions it is implied that these are single run results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in recommender systems, gradients, and temporal data.
