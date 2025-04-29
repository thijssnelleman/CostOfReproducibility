
## Contrastive and View-Interaction Structure Learning for Multi-view Clustering
Jing Wang, Songhe Feng
Keywords: Machine Learning: ML: Multi-view learning, Machine Learning: ML: Clustering
IJCAI/2024/Proceedings/0559 - Contrastive and View-Interaction Structure Learning for Multi-view Clustering.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a link to their implementation. They state on which OS the experiments were conducted and with which compute in the implementations section. They provide a large overview in figure 1, and pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors use six open data sets, state descriptions and give citations and give statistics on each data set in table 2. Download links / instructions are not provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors provide some details regarding the hyperparameters in the implementations section, and state the trade-off HPs are selected from a grid. Although few input parameters are stated in Algorithm 1, step 2 and 5 do indicate more HPs are present of which the values are not given. The authors state 'other baselines are implemented by the recommended .. parameters' in the implementation section suggesting that these values should be taken from the original work.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The authors state they use six widely used metrics in their method and provide a citation on their explanation. The authors do not state any details regarding training/testing splits of the data, but some training details are given in the implementations section. The results seem to indicate single runs/models.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a good understanding on multi-view learning. Furthermore, the presented framework has a few layers to it, and with the absence of the implementation documentation it will require either a good foundation of practical experience in the subfield or sourcing information from other works to reproduce the method.
