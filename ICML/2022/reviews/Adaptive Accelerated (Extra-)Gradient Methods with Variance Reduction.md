
## Adaptive Accelerated (Extra-)Gradient Methods with Variance Reduction
Zijian Liu, Ta Duy Nguyen, Alina Ene, Huy Nguyen
Keywords: 
ICML/2022/Proceedings/16531 - Adaptive Accelerated (Extra-)Gradient Methods with Variance Reduction.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors link an implementation from another work which they use for their experiments (https://github.com/bpauld/AdaSVRG). This makes evaluating this a bit difficult, as it is not their own implementation. However since this question is geared towards documentation provided by the authors and this is documentation, we will evaluate it as such. The readme has explanations on how to run the code and an explanation of the possible parameters. There is a dependencies file but not an installation file. The code has a decent amount of comments. The structure is large and can use an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use 4 benchmark data sets for which they provide a citation. A direct link is present in the implementation. No description or statistics given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors specify the hyperparmaeter search over grids in section 3 and which parameter they consider per method. The grid was searched per experiment and results are in table 2 of appendix E.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the methods over various loss functions and plot the mean and standard deviations. Its not clear how often the experiments were repeated. They plot training procedures.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with gradient methods.
