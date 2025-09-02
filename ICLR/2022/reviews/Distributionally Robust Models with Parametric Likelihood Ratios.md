## Distributionally Robust Models with Parametric Likelihood Ratios
Paul Michel, Tatsunori Hashimoto, Graham Neubig
Keywords: 
ICLR/2022/Proceedings/6425 - Distributionally Robust Models with Parametric Likelihood Ratios.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in footnote 1 of the abstract (https://github.com/pmichel31415/P-DRO). The readme contains an overview of the method, how to install the requirements, an example how to run the code with a link to their pretrained model, and how to run it with example configuration values and an explanation of some of them and how to cite the paper. The code contains a good amount of comments. The repository is large but is in general well organised with good names for files etc.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use 4 datasets: BiasedSST, FDCL18, Waterbirds and CelebA, provide citations and descriptions on them. The SST dataset is included in the repository including the splits. For the others no links are provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The hyperparameter values are summarised in text in appendix A. For some a acquisition strategy is specified (grid search, grid specified). General structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors report robust (worst) and averages test accuracies with standard deviations across 5 runs with different seeds. For one the split is included in the repository. For the others it is unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
