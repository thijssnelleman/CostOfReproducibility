
## Project and Forget: Solving Large-Scale Metric Constrained Problems
Rishi Sonthalia, Anna C. Gilbert
Keywords: 
JMLR/2022/Proceedings/201424 - Project and Forget: Solving Large-Scale Metric Constrained Problems.pdf
Project URL: https://github.com/rsonthal/ProjectAndForget

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation on the JMLR website and in footnote 1 in section 5 (https://github.com/rsonthal/ProjectAndForget). In the readme they state in which version of Julia it was made, an overview of each file and for which experiment it is used and what inputs the code uses. Code can use more comments. No installation instructions except for the Julia version which does not seem enough based on the imports in the notebooks.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors focus on two types of problems, metric nearness and correlation clustering. Both ar eexplained and sources cited. The authors generate synthetic data for the first (detailed and code in the implementation given), datasets for the second which are present in the implementation but little details are provided. In section 6 the authors use more synthetic data and state the generaton process but no code, for 6.2 the authors describe the problem and provide data files in the implementation, for 6.3 the authors generate more data, describe it and provide code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

For 6.2 the authors specify the hyperparameter values. The other methods are seemingly parameter free. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure time in seconds and used memory in general. For some problems they also measure task specific metrics. For 6.2 they specify the data split and present results on the test set. Results are single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on convex optimisation and constrained optimisation.
