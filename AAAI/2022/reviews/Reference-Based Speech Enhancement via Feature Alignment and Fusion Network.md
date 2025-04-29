
## Reference-Based Speech Enhancement via Feature Alignment and Fusion Network
Huanjing Yue, Wenxin Duo, Xiulian Peng, Jingyu Yang
Keywords: Speech & Natural Language Processing (SNLP)
AAAI/2022/Proceedings/21419 - Reference-Based Speech Enhancement via Feature Alignment and Fusion Network.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a source for their implementation (https://github.com/HieDean/FAF-Net). The authors provide an architecture scheme, details on the installation and a brief explanation how to run the code. There are a few comments in the code regarding sources, but more would be welcome. The repository is not that large, so its relatively little effort to go through but more documentation would help.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use two benchmark data sets which they cite, provide descriptions on and statistics. There are no direct links to the data sets in the repository, but they do provide the code used to handle the data. The authors do state they did manual labelling on one of the data sets, which is seemingly not published.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide the hyeparameters and architecture used in the training details. Details on how to run the training procedure are stated briefly in the implementation. No details are specified on how the hyperparameter values were determined. The authors do an ablation study on their method (stages).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The training procedure is explained, and the metrics for the evaluation summarised and cited. They present single model results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires good understanding on the type of network presented and some understanding of NLP / speech data.
