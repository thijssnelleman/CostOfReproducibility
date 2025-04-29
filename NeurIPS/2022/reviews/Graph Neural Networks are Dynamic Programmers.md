
## Graph Neural Networks are Dynamic Programmers
Andrew J Dudzik, Petar Veličković
Keywords: 
NeurIPS/2022/Proceedings/53143 - Graph Neural Networks are Dynamic Programmers.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide detailed pseudo code in appendix A and B. No implementation given. They state in section 7 they reuse publicly available code for the CLRS benchmark (citation given).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use the data generation from the CLRS benchmark (cited). There is a brief description of the benchmark. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state architecture details in section 7. Full hyperparameter overview missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

They measure out of distribution tests as metric. In appenix F table 3 they state the results are presented as averaged over 3 or 8 seeds (runs). The variance seems to be standard error but its a bit unclear. Generated data used.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on GNNs.
