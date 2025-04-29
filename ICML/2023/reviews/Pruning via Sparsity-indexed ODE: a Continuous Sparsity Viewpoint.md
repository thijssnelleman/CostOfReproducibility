
## Pruning via Sparsity-indexed ODE: a Continuous Sparsity Viewpoint
Zhanfeng Mo, Haosen Shi, Sinno Jialin Pan
Keywords: 
ICML/2023/Proceedings/25197 - Pruning via Sparsity-indexed ODE: a Continuous Sparsity Viewpoint.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/mzf666/sparsity-indexed-ode). In the repository they state installation instructions and where to find the scripts for running the experiments. The repository structure is very large and could use a better index. A lot of the code does not have comments. Pseudo code is available in algorithm 1 and more details can be found in appendix A.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use four benchmark datasets on which they provide citations. Details on the datasets are not given. The code has an automatic download function for all four it seems.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors summarise the hyperparameters per model/dataset in table 6 of the appendix. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate iterative magnitude pruning (a metric which is not standard but they do provide a citation on) and accuracy. Train/test split not applicable (nn pruning). Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in NN pruning.
