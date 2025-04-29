
## Seeded Graph Matching for the Correlated Gaussian Wigner Model via the Projected Power Method
Ernesto Araya, Guillaume Braun, Hemant Tyagi
Keywords: 
JMLR/2024/Proceedings/220402 - Seeded Graph Matching for the Correlated Gaussian Wigner Model via the Projected Power Method.pdf
Project URL: https://github.com/ErnestoArayaV/Graph-matching-PPMGM

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to the implementation on JMLR website (https://github.com/ErnestoArayaV/Graph-matching-PPMGM) and in footnote 3. In the readme they give an overview of the directory and what code can be used to reproduce which results. No installation instructions. Very few comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use simulated data in 5.1. and 5.2. (formulas and strategies provided), real data in 5.3. Code and data files present in the implementation. Data set is described but more details would be welcome. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Parameter is MC rollouts is given per experiment. For parameter τ the authors employ a grid search and present a heatmap with the results. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the CDF forumal definition in sec 5.3. They also use recovery fraction. Variation is 90% of the monte carlo runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on graph matching.
