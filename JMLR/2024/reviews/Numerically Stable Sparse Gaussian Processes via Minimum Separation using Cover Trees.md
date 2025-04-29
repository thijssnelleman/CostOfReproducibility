
## Numerically Stable Sparse Gaussian Processes via Minimum Separation using Cover Trees
Alexander Terenin, David R. Burt, Artem Artemev, Seth Flaxman, Mark van der Wilk, Carl Edward Rasmussen, Hong Ge
Keywords: 
JMLR/2024/Proceedings/221170 - Numerically Stable Sparse Gaussian Processes via Minimum Separation using Cover Trees.pdf
Project URL: https://github.com/awav/conjugate-gradient-sparse-gp

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation on JMLR website (https://github.com/awav/conjugate-gradient-sparse-gp). They also state it on the first page of the paper. In the readme they state installation instructions, how to run the code and an overview on the interface. Code needs more comments and an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use two datasets: East Africa and Combined Cycle Power Plant for which they provide descriptions and citations. There is a direct link in the readme for the UCI datasets but not for East Africa. No statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors give config files per experiment. There is no acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state how they split the data in appendix D for east africa. Each experiment was repeated 20 times. They plot mean with standard deviation in the figures. They measure RMSE, NLPD, ELBO and Condition Number but do not define the metrics (except for condition number).  Its not clear on what data split the results are eported on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on gaussian processes and cover trees.
