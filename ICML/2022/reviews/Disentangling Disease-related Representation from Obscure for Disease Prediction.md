
## Disentangling Disease-related Representation from Obscure for Disease Prediction
Chu-ran Wang, Fei Gao, Fandong Zhang, Fangwei Zhong, Yizhou Yu, Yizhou Wang
Keywords: 
ICML/2022/Proceedings/17211 - Disentangling Disease-related Representation from Obscure for Disease Prediction.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not publish their code. Some details are in section 4.1. In figure 3 there is an overview. In appendix C they state their implementation was done in PyTorch.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[8]

(1/4)

In appendix A the authors state details on each data set with statistics visualisation. They state in 4.1 they use one public data set (with citation) and three in house datasets. There are no acquisition strategies given, nor proper descriptions. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors propose a framework in their method, but no HP values of the methods they use.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state they split the data in tvt by 80/10/10, but its not clear how this is done (Random or static?). The authors use AUC as a metric. The results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on biomedical research, disentangled representation learning. 
