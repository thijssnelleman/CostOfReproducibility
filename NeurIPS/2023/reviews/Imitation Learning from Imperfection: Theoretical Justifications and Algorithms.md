
## Imitation Learning from Imperfection: Theoretical Justifications and Algorithms
Ziniu Li, Tian Xu, Zeyu Qin, Yang Yu, Zhi-Quan Luo
Keywords: 
NeurIPS/2023/Proceedings/70103 - Imitation Learning from Imperfection: Theoretical Justifications and Algorithms.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/liziniu/ISWBC). They provide three seperate readmes per dataset/simulator. Each contains installation notes, direct download links for the datasets and how to run the code + acknowledgements for the implementation. The code could use some more/better comments. The strcuture is well organised with the seperate readmes.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors provide direct links in each readme for datasets.  In 6.1. they state the eivnornments used from MuJoCo (citation, auto install in implement). The tasks are not described for the environments. Dataset is described in H1.3. statistics are minor.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discus the hyperparameters/architecture details in H.1. per experiment. Structured overview is presented per experiment in the implementation. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results as mean + std dev over 5 random seeds. Metric is environment return for the RL tasks and accuracy for table 4. The data split for table 4 is given H.1.3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise in RL (+ theory) and imitation learning.
