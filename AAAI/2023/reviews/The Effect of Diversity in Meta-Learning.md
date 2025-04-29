
## The Effect of Diversity in Meta-Learning
Ramnath Kumar, Tristan Deleu, Yoshua Bengio
Keywords: ML: Meta Learning, ML: Multi-Instance/Multi-View Learning, ML: Representation Learning, ML: Transfer, Domain Adaptation, Multi-Task Learning, ML: Active Learning, ML: Optimization, ML: Deep Neural Network Algorithms, ML: Other Foundations of Machine Learning, ML: Classification and Regression, ML: Evaluation and Analysis (Machine Learning)
AAAI/2023/Proceedings/26012 - The Effect of Diversity in Meta-Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share their implementation source (https://github.com/RamnathKumar181/Task-Diversity-meta-learning). It includes installation notes for the requirements, the data sets should automatically be downloaded upon running the code. The meta data sets have download instructions and more options are given to the reader. The authors provide training and testing scripts and how to run them. Scripts regarding metric calculation and analysis are also provided. The code base is rather large but has a lot of comments in the code. Data loaders are also provided. A general directory structure diagram/explanation is missing, but in general it is very well documented.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors give clear explanation on how to acquire the four used data sets in the implementation documentation. Citations on the data sets are provided and more details could supposedly be found in the missing appendix (AAAI requirements). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state hyperparameter details can be found in appendix B. This can not be found in the paper nor the implementation documentation. However with some effort these values can be extracted from the implementation. How these values are acquired is unclear, but if the appendix were given this would perhaps answer this question too. With the appendix (if expected details are there), this value should be 1-2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state clearly what the questions are they aim to answer with the experiments. They state on which data sets they train, and under what circumstances (20-shot 1 way) the results were acquired. The authors state they use accuracy as a metric in the figure caption. Wit hthe presence of the implementation, all needed information is provided.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding of meta learning, but the documentation is very complete thus aiding independent investigators in understanding the method for reproducing it.
