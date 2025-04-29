
## Misspecified Phase Retrieval with Generative Priors
Zhaoqiang Liu, Xinshao Wang, Jiulong Liu
Keywords: 
NeurIPS/2022/Proceedings/55168 - Misspecified Phase Retrieval with Generative Priors.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their code in the supplementary material (https://openreview.net/attachment?id=--aQNMdJc9x&name=supplementary_material). Pseudo code in algorithm 1. In the readme they state installation notes, how to run the code for their experiments with arguments. The code needs more comments. The structure is very large and needs an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use MNISt and CelebA, but only present MNIST in the main paper. Citation is provided and a description given in section 5. No direct link or detailed statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss the hyperparameters used in section 5. They are given per experiment in the readme (structured). Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors report results on 10 instances of the static test sets, they also perform 10 random restarts and average over all. They measure reconstruction error as metric but do not define it. The variation in fig 2 is not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on retrieval and reconstruction.
