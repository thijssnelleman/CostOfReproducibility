
## Gap Minimization for Knowledge Sharing and Transfer
Boyu Wang, Jorge A. Mendez, Changjian Shui, Fan Zhou, Di Wu, Gezheng Xu, Christian Gagné, Eric Eaton
Keywords: 
JMLR/2023/Proceedings/220099 - Gap Minimization for Knowledge Sharing and Transfer.pdf
Project URL: https://github.com/bwang-ml/gapBoost

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website (https://github.com/bwang-ml/gapBoost). In the readme they state where to download a toolbox and datasets and how to run the code. There is also an installation note. Code has okay comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(7/7)

The authors state one dataset download links in the implementation readme. They use Newsgroups and Office-Caltech in the paper for gapBoost and they are described (Office with citation) but statistics are very minor. And for gapBoostR they use Concrete, Housing, AutoMPG, Diabetes and Friedman (link provided for the first three, citation for the fourth and fifth) but no description / statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state in 6.1. the hyperparameters for gapBoost as a formula and motivate it theoretically. They conduct an analysis on it in figure 3. More details givein appendix C.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors report the results in terms of average error rate percentage and standard error over 5 classification tasks. Each experiment was repeated over 20 random train/test splits, and the proportion seems to be 10-90.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on transfer learning.
