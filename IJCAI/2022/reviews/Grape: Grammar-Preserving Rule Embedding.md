
## Grape: Grammar-Preserving Rule Embedding
Qihao Zhu, Zeyu Sun, Wenjie Zhang, Yingfei Xiong, Lu Zhang
Keywords: Natural Language Processing: Applications, Natural Language Processing: Language Generation, Natural Language Processing: Natural Language Semantics
IJCAI/2022/Proceedings/0631 - Grape: Grammar-Preserving Rule Embedding.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/pkuzqh/Grape). The authors state in the readme how to run the code briefly. No other information is provided. The code has some decent comments, but a lot of the files also have none. There is quite a lot of code files, but its a single directory so its still overseeable. The implementation could definetily do with more documentation. They state in the paper the parsers used for their method with direct links to it.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors state they use 6 benchmark datasets in their paper, provide citations on them, state statistics in table 1, and a description on each in 3.1. The data is not present in the implementation docs and no direct links are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameter values in 3.1, and the space can be checked with some effort in the implementation. The authors state 'we selected the values based on validation score' (human optimisation / empirical) but the budget is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors discuss the metrics used in 3.1 briefly per benchmark (experiment), provide citations on them and short descriptions. Although it is not clearly defined in their work, they do clearly state that these are defined in the previous (cited) work. The authors state they repeated the folds five times for three benchmarks ("due to the small validation set size"), explaining the aggregation + variation for limited results in table 2. The aggregation + variation method for these is not explained. The train/validation/test sets are fixed as shown in table 1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience in NLP and deep NNs, as well as previous works on the (new?) task (grammar preserving rule embedding).
