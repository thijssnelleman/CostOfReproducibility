
## A Unified Framework for Optimization-Based Graph Coarsening
Manoj Kumar, Anurag Sharma, Sandeep Kumar
Keywords: 
JMLR/2023/Proceedings/221085 - A Unified Framework for Optimization-Based Graph Coarsening.pdf
Project URL: https://github.com/GraphCoarsening/Featured-Graph-Coarsening.git

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link on the JMLR website (https://github.com/GraphCoarsening/Featured-Graph-Coarsening). In the readme they describe, unstructured, what code regarding the experiments can be found where. There are some installation instructions in the notebooks. Needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(11/11)

The authors list the datasets used in section 7, with statistics and generation parameters. Descriptions lacking. One dataset is present in the implementation but does not seem to be used in the experiments, generator code provided. No citation or direct links for the other datasets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values of the pseudo code per data set. Acquisition not specified

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure loss, epsilon similarity (defined in eq. 9), REE, DE (Explained in 7.1). Evaluations are on the entire dataset (no split). Single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on graph coarsening.
