
## Adaptive False Discovery Rate Control with Privacy Guarantee
Xintao Xia, Zhanrui Cai
Keywords: 
JMLR/2023/Proceedings/230039 - Adaptive False Discovery Rate Control with Privacy Guarantee.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

No implementation given. The authors do refer to a package with citation they use for processing data.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

In section 4.1 the authors use simulated data and refer for it to a previous work. The parameters are provided and formulas per experiment but the implemetation is not given. In 4.3 they use the Bottomly dataset, describe it with a citation but no link or other details regarding the dataset but processing is explained.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method is seemingly parameter free asside from the target FDR level alpha which they vary over in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

In figure 2-9 present results averaged over 100 trials, with metrics FDR (eq 1.), Power (defintion 2). Table 1 presents computations time in second averaged over 100 replications. In figure 10 they measure the number of rejections (sec 1.2) over target FDR level. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires experience with FDR and differential privacy.
