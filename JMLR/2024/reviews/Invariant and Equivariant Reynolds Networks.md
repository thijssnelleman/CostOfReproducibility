
## Invariant and Equivariant Reynolds Networks
Akiyoshi Sannai, Makoto Kawano, Wataru Kumagai
Keywords: 
JMLR/2024/Proceedings/220891 - Invariant and Equivariant Reynolds Networks.pdf
Project URL: https://github.com/makora9143/ReyNet

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a project link on the JMLR website (https://github.com/makora9143/ReyNet). In the readme they state a list overview of included materials in the implementation, a download link to datasets, an overview of the data structure. There is an installation requirements file. The code needs more comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(10/10)

The authors provide a download link in the implementation for the datasets. This is provided for 8 datasets and there is also a synthetic generator in the code. The synthetic generation is given in 8.1. The datasets are cited in 8.2. and described in appendix C. No statistics. Finally they also use Mol-HIV from OGB. they provide a citation and brief description but no statistics or download link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters are organised in the code but not kept in seperate files. They specify them per method/dataset. They are described in 8.2. but no acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Data split is given in 8.1 for synthetic generation and in 8.2. they state they use 10-fold on which they report average accuracy + std dev.  For the synthetic dataset they report MSE.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on geometric deep learning. 
