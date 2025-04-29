
## Continuous Treatment Effect Estimation Using Gradient Interpolation and Kernel Smoothing
Lokesh Nagalapatti, Akshay Iyer, Abir De, Sunita Sarawagi
Keywords: ML: Causal Learning
AAAI/2024/Proceedings/30553 - Continuous Treatment Effect Estimation Using Gradient Interpolation and Kernel Smoothing.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation source in the abstract (https://github.com/nlokeshiisc/GIKS_release). They provide the 2 datasets in the repository and a link to three others. They describe how the code can be run, where the code for four baselines are found and the repository of two others are linked. They show where the evaluation code can be found of all data sets and a note book where the paper's plots are made. The code has some comments but could certainly use more, as there are many constant definitions that could be helped with some explanations. A data loader/processor is present too. The paper has pseudo code of the algorithm. An explanation of the implementation structure is missing (visualisation or general explanation in the readme). There is also no description of dependencies such as a requirements.txt.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors provide sources in the implementation documentation for each data set including data loaders and processors. The authors provide no statistics on the data sets but do cite the sources in their paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state they use three hyperparameters that they optimise using grid search. They do not state any budget, indicating its been exhaustively searched based on the table and results presented. There are possibly more hyperparameters that have been set, which could be extracted from the implementation documentation with some effort. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors denote which evaluation metrics they are using with explanations. The results seem to indicate one-shot, but this is not stated specifically.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method is relatively compelx and requires a good understand of mathematics (gradients and statistics specifically). However it is well documented and an implementation is provided. This cost could have been even lower if the implementation documentation was more extensive.
