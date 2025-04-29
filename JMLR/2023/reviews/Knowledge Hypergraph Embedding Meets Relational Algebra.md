
## Knowledge Hypergraph Embedding Meets Relational Algebra
Bahare Fatemi, Perouz Taslakian, David Vazquez, David Poole
Keywords: 
JMLR/2023/Proceedings/22063 - Knowledge Hypergraph Embedding Meets Relational Algebra.pdf
Project URL: https://github.com/baharefatemi/ReAlE

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state a link to their implementation in the JMLR website (https://github.com/baharefatemi/ReAlE) and also in section 4. The also state in appendix E the implementation of baselines. In the readme they state a description on the implementations, dependencies, installation/compilation instruction, description on each parameter, how to run training, and contact details. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors provide a dataset synthesizer in the implementation and 4 datasets (FB-AUTO, FB15K, JF17K, REL-ER) three of which are used in sec 6.1 and cited. Statistics given on them in table 1, but no descriptions. In 6.2. the authors state a synthetic dataset and describe the decision for the generation process and detail it with algorithm 1 and 2. The code is available in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state they conduct each experiment with the best hyperparameters. In appendix D its stated tuning was done on the validation set. They tune lr, w, sigma on specified grids. In section C.1. they fixed two HP settings based on all other baselines but why is not clear. The selected values are also not stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate each experiment 10 times and report the mean (MRR is a mean metric) and the standard deviation in table 2. Other metrics are Hit@k (not explained). The authors state t/v/t generation for the synthetic data. In table 1 the authors indicate the datasets have static splits provided and these are also seperate available in the implementation link. Its not clearly specified in each result on what set the result is on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on knowledge hypergraphs.
