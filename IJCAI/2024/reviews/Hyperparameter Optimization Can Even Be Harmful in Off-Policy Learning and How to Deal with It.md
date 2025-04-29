
## Hyperparameter Optimization Can Even Be Harmful in Off-Policy Learning and How to Deal with It
Yuta Saito, Masahiro Nomura
Keywords: Machine Learning: ML: Causality, Machine Learning: ML: Hyperparameter optimization, Machine Learning: ML: Multi-armed bandits, Uncertainty in AI: UAI: Causality, structural causal models and causal inference
IJCAI/2024/Proceedings/0537 - Hyperparameter Optimization Can Even Be Harmful in Off-Policy Learning and How to Deal with It.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors state and link the toolkit they use for their empirical analysis. The authors state in section 4.3 that 'our algorithm is easy to implement with a few additional lines of code'. No source for their implementation can be found. Although the base for their implementation is given (toolkit), many details may still be found in the implementation documentation, thus it still brings some cost with it. The authors provide two pseudo code for their method, which definetily does help.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use synthetic data generation for which they include a link to the source and conditions under which it was generated. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors anaylse the impact of hyperparameter optimisation for off-policy learning. For this they extensively discuss the various hyperparameters in their method and do ablation studies on them. Budgets are discussed per experiment and the search spaces / grids per parameter. The approaches / models used to search these spaces are defined. The appendix contains tabular information on the spaces and results.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the parameter grids and trials for the experiments, and in figure 1 they state how many runs were done (over random seeds) and how these are aggregated. The authors seem to measure 'relative gen policy performance', but this is not clearly stated with each result. With a bit of effort this could be determined.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a thorough understanding of both off policy learning and HPO to understand the stated problem and the analysis.
