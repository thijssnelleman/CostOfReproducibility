
## Preserving Fairness in AI under Domain Shift
Serban Stan, Mohammad Rostami
Keywords: 
JAIR/2024/Proceedings/16694 - Preserving Fairness in AI under Domain Shift.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the introduction (https://github.com/rostami-m/FairUDA/). In the readme there is a short note on installation but its not very clear. Code can use more comments in some files.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors state the three datasets used in 5.1.1. with a description and direct links in the footnotes. Statistics are a bit lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss the hyperparameters in 5.1.5. and a full summary can be found per dataset in the config.py file in the implementation. The acquisition is not completely clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors explain the datasplit in 5.1.2. and analyse it in table 1.  The metrics are stated in 5.1.3. Results are averaged over 7 runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise in fairness and domain shift.
