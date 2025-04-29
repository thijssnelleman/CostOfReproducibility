
## Scalable Coupling of Deep Learning with Logical Reasoning
Marianne Defresne, Sophie Barbe, Thomas Schiex
Keywords: Machine Learning: ML: Neuro-symbolic methods, Constraint Satisfaction and Optimization: CSO: Constraint learning and acquisition, Multidisciplinary Topics and Applications: MDA: Bioinformatics
IJCAI/2023/Proceedings/0402 - Scalable Coupling of Deep Learning with Logical Reasoning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://forgemia.inra.fr/marianne.defresne/emmental-pll). In the readme they state installation instructions, a folder structure, direct download links to the data sets and where they should be placed, how to run training/testing with possible arguments/options, how to run the exact experiment from the paper, and some more instructions regarding training/experiments. The code has a decent amount of comments. They provide details on the implementation in section 5 of the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors provide direct download links for the datasets in the implementation docs. The authors use the soduku problem as benchmark. The authors cite the data set source in section 5.1 and discuss the problem in detail. They also state what subset of the data they use.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss a hyperparameter k and grid evaluate it in table 1. They state their hyperparameters in introduction of sec 5 and state 'other parameters take default values'. There is no explanation/defence/search done or specified for these parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state their train/validation/test splits in the data set explanation. The results are single run/model. The metrics are explained and either standard or problem related.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires an understanding of deeplearning and logic reasoning/explanation as well as experience with the proofs stated.
