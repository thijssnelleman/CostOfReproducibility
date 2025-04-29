
## Interventional SHAP Values and Interaction Values for Piecewise Linear Regression Trees
Artjom Zern, Klaus Broelemann, Gjergji Kasneci
Keywords: ML: Transparent, Interpretable, Explainable ML, GTEP: Cooperative Game Theory, ML: Classification and Regression, PEAI: Interpretability and Explainability
AAAI/2023/Proceedings/26322 - Interventional SHAP Values and Interaction Values for Piecewise Linear Regression Trees.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present a link to their implementation (https://github.com/schufa-innovationlab/pltreeshap). The implementation has clear installation notes and how to use it. The comments are impressive in terms of frequency and quality, and believe this should be part of some larger library. Furthermore, the authors provide extensive pseudo code in their paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a public available data set, provide citations on them and a direct download link. Furthermore some details and statistics on the data set are provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state they do a grid search over two parameters, indicating they did it exhaustively. However, the selected values are not clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors take the average over 10 runs over 100 instances. They explain the runtime evaluation of each experiment. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The authors extend decision trees with their new algorithm, requiring extensive knowledge on the mathematics they discuss.
