
## Globally Gated Deep Linear Networks
Qianyi Li, Haim Sompolinsky
Keywords: 
NeurIPS/2022/Proceedings/53916 - Globally Gated Deep Linear Networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their code in the supplementary materials (https://openreview.net/attachment?id=hqRwcqzegr7&name=supplementary_material). There is no readme present. No installation notes. The code needs more comments. Structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use MNIST as a dataset and provide a citation. In appendix C.3 they give some details on the dataset and C.4. their permutations. The code for permutation is included in the implementation and parameters are given. No statistics or link to MNIST.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors define the parameters used for their method in appendix C (informally). The values are also stated in the implementation per experiment file. The acquisition is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The metrics are error rate and ratio, population parameters are specified, results are over training, aggregation is average. Variance unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on activation functions and non lineartiy in NNs.
