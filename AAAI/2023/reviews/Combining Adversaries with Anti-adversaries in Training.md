
## Combining Adversaries with Anti-adversaries in Training
Xiaoling Zhou, Nan Yang, Ou Wu
Keywords: ML: Adversarial Learning & Robustness, ML: Bias and Fairness, ML: Classification and Regression, ML: Deep Learning Theory, ML: Meta Learning
AAAI/2023/Proceedings/26352 - Combining Adversaries with Anti-adversaries in Training.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors present a theoretical investigation. The present pseudo code on their proposed algorithm. However, although this proposed algorithm is only a part of the presented work, its implementation is still relevant to the presented results. As the authors provide zero details on their implementation, it would have to be done with the sole aid of the pseudo code and descriptions in the paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors state they use three data sets which are public and provide citations on them. However, statistics/descriptions or details are missing on them and no direct link is provided nor details on processing/loading.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the details on their hyperparameter values in the experiments section, and one parameter value is explored on a grid. They also refer to another work regarding details on their hyperparameter tuning method. It is not entirely clear whether all necessary hyperparameters are given for comparison due to the missing implementation documentation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state their training procedure. They shortly note which metrics (error rates) they will use but do not state full definitions. For testing the authors refer to another work. In general it should not be too much effort but will require some checking.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a very deep understanding of adverserial learning and the theory behind it, but also an adept level of meta learning. The lack of implementation worsens this somewhat.
