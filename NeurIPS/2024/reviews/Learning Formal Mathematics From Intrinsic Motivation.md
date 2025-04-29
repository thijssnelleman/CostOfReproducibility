
## Learning Formal Mathematics From Intrinsic Motivation
Gabriel Poesia, David Broman, Nick Haber, Noah Goodman
Keywords: 
NeurIPS/2024/Proceedings/93276 - Learning Formal Mathematics From Intrinsic Motivation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/gpoesia/minimo). In the readme they provide instllation instructions, tutorials for the languages and apis, how to run the experiments and point to the configuration files for it. In general the code has good comments although some files or functions are completely without. The structure is large and could use an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The method generates problems and solves them. In 3.1 the generation task (conjecturing) is described. It generates various types of data described. The generator is included in the implementation. The amount of data generated per experiment is stated in section 4, but exact parameters are not clear. The authors also use human written data in sec 4.2. where they state they take theorems from a text book which they cite and the natural number game (also citation provided). The latter data set is available in the implementation. The former is not there, but is considered public as its in a book however the cost acquisition of the data is higher. It is well described however how this data is acquired from the book

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide various configuration files in the implementation. In appendix A the authors state training details with the values which can also be found summarised in these files. The authors state they 'found these parameters' which implies emperical but no budget given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present their results over 3 random seeds with standard error bands. Metric is log likelihood. The aggregation is not specified only variation. In figure 4 the metric is success rate and provide a single run. No split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise in automated mathematical formula solving and proofs.
