
## Dimension Reduction and MARS
Yu Liu LIU, Degui Li, Yingcun Xia
Keywords: 
JMLR/2023/Proceedings/221422 - Dimension Reduction and MARS.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in section 4 (https://github.com/liuyu-star/drMARS). In the readme they state how to use the code, give details on the datasets with download links and contact details. Code has okay comments. No installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

The authors provide two download links in the readme of the implementation, there are also some datasets included. In section 4 they conduct simulation studies and state the data generation models with parameter values (generator included in code). In section 5 they conduct experiments on 7 datasets and provide direct links for each, a description and some high level statistics. Information on each dataset can be a bit better.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors determine the SDR space dimension using CV. The authors state that 'For all the R functions their default values of tuning parameters are used'. Its unclear what these values are. Some parameters are described in text, but a full overview on the selected values are unclear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results as average over 100 replications and detail the data split (randomly per run) in sec 5. The authors also apply 10-fold cv with random split to select the 'dimension of SDR space'. Metrics are defined in sec 5 and 6.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on gardient estimation and dimension reduction.
