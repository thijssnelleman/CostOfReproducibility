
## SGD with Coordinate Sampling: Theory and Practice
Rémi Leluc, François Portier
Keywords: 
JMLR/2022/Proceedings/211240 - SGD with Coordinate Sampling: Theory and Practice.pdf
Project URL: https://github.com/RemiLELUC/SCGD-Musketeer

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors providy a link to their implementation on the JMLR website and in footnote 1 (https://github.com/RemiLELUC/SCGD-Musketeer). In the readme they give an extensive overview on the files and point to an installation requirements file. Code could use some more/better comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use both synthetic data and real data in section 5. MNIST, Fashion-MNIST are both cited and readily available in the code (direct link) but descriptions are lacking. The synthetic data is briefly described, but variables and code is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The hyperparameter values given in the code but requires some digging (no easy structured file like config.yaml). No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the methods on optimality gap (formula given), training loss and test accuracy. Based on the code they use the standard splits of the data. For the real data they present mean and standard dev over 10 independent runs. The synthetic data presents the results over 20 independent simulations averaged.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on SGD.
