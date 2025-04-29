
## Graph Disentangled Contrastive Learning with Personalized Transfer for Cross-Domain Recommendation
Jing Liu, Lele Sun, Weizhi Nie, Peiguang Jing, Yuting Su
Keywords: DMKM: Recommender Systems
AAAI/2024/Proceedings/29398 - Graph Disentangled Contrastive Learning with Personalized Transfer for Cross-Domain Recommendation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide no source for their implementation documentation. They do state that it was made with PyTorch, followed by several HP values. A large schematic of the model is provided and a small illustration of the cross domain recommendation of their framework compared to others.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use a publicly available data set and link a url to where it can be found. Statistics on the data is provided in tabular format. Key details were provided on how the data was used, but exactly how the data was processed/loaded is unclear. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Key hyperparameters and semantic parameters are provided in the implementation section. It is unclear if these are all needed hyperparameters and the lack of implementation documentation could increase required efforts. No specification on the acquisition of these hyperparameter values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide their evaluation strategy (leave-one-out) with the amount of repetitions. The metrics used are shortly described.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

The method deals with recommender systems in combination with graph based data / learning. The techniques require a good understanding of the underlying (matrix) mathematics and the outline of the framework seems quite daunting. Independent investigators need to have or acquire a lot of expertise before reproducing this work. This is substantially worsened by the lack of implementation.
