
## Interpretable and Fair Boolean Rule Sets via Column Generation
Connor Lawless, Sanjeeb Dash, Oktay Gunluk, Dennis Wei
Keywords: 
JMLR/2023/Proceedings/220880 - Interpretable and Fair Boolean Rule Sets via Column Generation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(16/16)

The authors use 15 classification data sets from UCI repository (citation provided, direct link in reference). They also use FICO dataset (Citation + link in references). The latter is described in 5.1. More details are in appendix B. Not each dataset is described with text but all have some details. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperaprameters were tuned using 10-fold cross-validation. Overview of the grids used for HP testing is in tables in appendix O. Selected values unclear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors give test performance on all datasets using 10-fold stratified cross-validation. The authors report average + standard deviation over accuracy. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on fair machine learning.
