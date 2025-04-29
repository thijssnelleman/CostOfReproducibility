
## D-GCCA: Decomposition-based Generalized Canonical Correlation Analysis for Multi-view High-dimensional Data
Hai Shu, Zhe Qu, Hongtu Zhu
Keywords: 
JMLR/2022/Proceedings/20021 - D-GCCA: Decomposition-based Generalized Canonical Correlation Analysis for Multi-view High-dimensional Data.pdf
Project URL: https://github.com/shu-hai/D-GCCA

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website and in the introduction (https://github.com/shu-hai/D-GCCA). In the readme they give an introduction on the method, and refer to a file for an example. No installation instructions. Structure is simple. Comments are good.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors provide three datasets in their implementation and use it in example. Simulation studies are conducted in 4.1 and formulae/variables and values are provided in 4.1. The generator code is not provided. It is not clear if these files are the ones used in the experiments. The authors use real world datasets in section 5, provide citations on them and a description but stattistics could be better and no link. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors note parameters of the method in the code and various statements about their values are made in 4.1. however an overview is missing and its unclear what each parameter is and how they are acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Each experiment setting is replicated 1000 times independently and presented with average error for the simulations and table 1 also presents ortogonal pair, scaled squared errors with standard deviations. Table 2 uses SWISS scores which is defined on page 28, results are single run. Table 3 has corrleation scores.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on multi-view data and correlation analysis.
