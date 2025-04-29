
## Memory-Based Meta-Learning on Non-Stationary Distributions
Tim Genewein, Gregoire Deletang, Anian Ruoss, Li Kevin Wenliang, Elliot Catt, Vincent Dutordoir, Jordi Grau-Moya, Laurent Orseau, Marcus Hutter, Joel Veness
Keywords: 
ICML/2023/Proceedings/23662 - Memory-Based Meta-Learning on Non-Stationary Distributions.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their code online (https://github.com/google-deepmind/nonstationary_mbml). In the readme they introduce the method, describe what the implementation is based on, index the repository structure, installation instructions and an example of running experiments and how the configurations can be adjusted. The code is rich in comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use four diferent distributions for synthetic data generation that they describe in section 6 and equation 1. The code for this is available in the implementation. The parameters are given either by default in section 6 or per experiment.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors discuss the architectures and hyperparameters in appendix A. They did an ablation study to determine the settings, by running 5 different seeds for each HP set. The possible settings are defined in the text over grids. The results can be seen in figure 7 and 8. A clear overview (table) of the selected paramters is not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metric is mean cummulative regret. The metrics are calculated over 10k sequences and they are repeated over 10 different random initialisations.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in bayesian inference, meta-learning.
