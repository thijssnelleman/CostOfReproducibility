
## Semiparametric Inference For Causal Effects In Graphical Models With Hidden Variables
Rohit Bhattacharya, Razieh Nabi, Ilya Shpitser
Keywords: 
JMLR/2022/Proceedings/20296 - Semiparametric Inference For Causal Effects In Graphical Models With Hidden Variables.pdf
Project URL: https://ananke.readthedocs.io/en/latest/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state in section 8 the R code is available upon request and in footnote 6 provide a link to their Python implementation documentation which is also linked on the JMLR website where the GitLab is linked (https://gitlab.com/causal/ananke/). They provide installation instructions, many tutorials, detailed documentation of the code and a structured overview.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors use simulated data in their experiments (4 different simulation experiments). The generation is explained and the parameter values given. The authors provide simulated datasets in their implementation, but its unclear if these are the datasets that are used. No generator found. More details regarding the simulated data given in appendix G.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method only uses input data, no parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present the results averaged over 100 iterations and report the absolute value of the bias with error bars representing standard error of the mean Other plots show boxplots. No data split. The metrics are bias and double robustness but are not clearly defined (no formula found).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on DAGs, and doubly robust estimation.
