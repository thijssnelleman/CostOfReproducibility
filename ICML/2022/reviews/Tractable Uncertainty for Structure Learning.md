
## Tractable Uncertainty for Structure Learning
Benjie Wang, Matthew Wicker, Marta Kwiatkowska
Keywords: 
ICML/2022/Proceedings/18117 - Tractable Uncertainty for Structure Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their implementation online (https://github.com/wangben88/trust). In the readme they introduce the method, provide installation instructions, how to ruin an experiment with arguments explanation and a repository index. Code in the trust directory: A lot of the python code has very good comments, the cpp code is a bit lacking but is relatively small part of the code base. The other directories contain (somewhat modified) versions of other implemntations they use in their work for comparison and thus not too relevant.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors generate data for their method. The generation parameters are specified. The code is available in the implementation. The distributions are specified in section 4 and appendix F.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameters in appendix F. The authors state they were selected empirically (acquisition, no budget). Overview is missing. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the used metrics with explanations, formulas and citations in 6.1. The authors state the training set generation in sec 6. and the test generation in 6.1. The experiments were run over 30 runs with mean and standard deviation reported. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on bayesian structure learning and tractable uncertainty.
