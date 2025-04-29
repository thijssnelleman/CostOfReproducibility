
## Personalized PCA: Decoupling Shared and Unique Features
Naichen Shi, Raed Al Kontar
Keywords: 
JMLR/2024/Proceedings/220810 - Personalized PCA: Decoupling Shared and Unique Features.pdf
Project URL: https://github.com/UMDataScienceLab/Personalized_PCA

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to the implementation on the JMLR website (https://github.com/UMDataScienceLab/Personalized_PCA). In the readme they give examples on how to run the experiments, links to download datasets, an overview on the file structure. No installation instructions. Code can user more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use a synthetic dataset in 7.1 and specify the generation model and parameters. Its not clear whether this is given in the implementation. In 7.3. they apply FEMNIST and CIFAR10 for which they provide citations and descriptions and some high level statistics. Download link in the repository.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters per experiment are specified in ppca.py of the implementation. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure log reconstruction error. The data set experiments are repeated 3 times and show the mean and std dev. The authors use training and test sets and show results on both of them, data splits given in 7.3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on PCA.
