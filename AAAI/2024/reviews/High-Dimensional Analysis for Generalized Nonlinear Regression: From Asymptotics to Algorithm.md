
## High-Dimensional Analysis for Generalized Nonlinear Regression: From Asymptotics to Algorithm
Jian Li, Yong Liu, Weiping Wang
Keywords: ML: Deep Learning Theory, ML: Deep Learning Algorithms
AAAI/2024/Proceedings/30366 - High-Dimensional Analysis for Generalized Nonlinear Regression: From Asymptotics to Algorithm.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their GitHub implementation (https://github.com/superlj666/NonlinearHDA). They also state more proofs and experiments can be found in the appendix of the full version which they link (https://lijian.ac.cn/files/2024/NonlinearHDA.pdf) but this file cannot be found currently. The implementation states under which environment the code should be run. There is a short description of the core functions in the repository, indexing which file handles what. They also link to a download for the data set. Instructions on how to run are provided, albeit short, as well as how to obtain the results from the experiments section of the paper including figure generation. The code is largely without comments, which decreases interpretability. There is also a notebook included for plots generation, however this only consists of code blocks (without comments) and titles. A short note is made about the implementation in the paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors shortly state they draw examples from the MNIST data set and cite the source. This is a well known publicly available data set, but no description on it is given which could pose hidden issues for reproducing. A URL is provided for downloading datasets in the implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state they do a, presumably exhaustive, grid search over two hyperparameter ranges. A few other parameters are noted in the section afterwards with fixed values. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state that they draw 100 random training examples from the MNIST data set. The test set size is difficult to make out, and its not specifically stated how many times the procedure was executed. The metrics are clear. Perhaps more details can be extracted from the implementation documentation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The mathematics in this method require a very good understanding to completely reproduce the method. This is not for a lack of trying by the authors, the documentation given is clear and with good instructions and analysis, rather it is a complex concept.
