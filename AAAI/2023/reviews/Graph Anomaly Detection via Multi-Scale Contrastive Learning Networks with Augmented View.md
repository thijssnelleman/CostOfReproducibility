
## Graph Anomaly Detection via Multi-Scale Contrastive Learning Networks with Augmented View
Jingcan Duan, Siwei Wang, Pei Zhang, En Zhu, Jingtao Hu, Hu Jin, Yue Liu, Zhibin Dong
Keywords: ML: Multi-Instance/Multi-View Learning, ML: Graph-based Machine Learning
AAAI/2023/Proceedings/25591 - Graph Anomaly Detection via Multi-Scale Contrastive Learning Networks with Augmented View.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/FelixDJC/GRADATE). They provide a readme with an overview on the method, contact details, overall framework illustration, requirements for the environment and a quickstart (albeit very 'concise'). The code has no comments (or practically none). The amount of files and directories is few which does make it easy to oversee. They provide pseudo code on the method in the paper. Data processing is done in the implementation and they ship one data set with it. The code would improve with more comments and the entire repo would do better under a more extensive readme, however all key elements are there and they can be reverse engineerd where necessary.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors use six benchmark data sets and provide statistics on them and citations. One of the data sets is directly available in the implementation source. Download instructions on the other data sets are not given and have to be determined.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

There are a few nodes on the model architecture in the experiments section. There is a sensitivty analysis on three balance hyperparameters and a modular ablation study on the method. Default values of other hyperparameters can be extracted with some effort from the implementation. No details are given on how these values are acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The metrics presented in the experiments are standard, however it is only noted that these are used without description. No notes are given on the train / test set split. The results seem to be single model/run but it is unclear. These details are seemingly ommited which have to be re-determined by independent investigators.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires some understanding of graph-based data tasks, and a good understanding of multi view learning.
