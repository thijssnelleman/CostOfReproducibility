
## Data-Free Hard-Label Robustness Stealing Attack
Xiaojian Yuan, Kejiang Chen, Wen Huang, Jie Zhang, Weiming Zhang, Nenghai Yu
Keywords: CV: Bias, Fairness & Privacy, ML: Privacy
AAAI/2024/Proceedings/28994 - Data-Free Hard-Label Robustness Stealing Attack.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their source code (https://github.com/LetheSec/DFHL-RS-Attack). They give a framework illustration, a link to their model checkpoints, and a link to 'performing attacks from scratch'. The readme has instructions on how to run the code. The code has generally few comments, and explanations could be broader. But in general, it offers decent help for re-implementing the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use two commonly used benchmark data sets, and cite them. No metrics are provided on the data sets, and there are no clear instructions (direct links) on how to acquire them or use them with the implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide the values used for their hyperparameters for each setting clearly, and if certain values are missing they could possibly be extracted from the implementation documentation. It is however unclear how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors briefly introduce and motivate the metrics used. The exact procedure seems to be unclear, but only single values are reported in the tables. With some effort the procedure could perhaps be extracted from the implementation documentation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The authors present a method regarding stealing model robustness, which is a clearly explained concept. The method is relatively straight forward, but certain topics and analysis in this domain require some experience. Furthermore, the tasks of the models and data are only briefly discussed and would require some expertise to understand.
