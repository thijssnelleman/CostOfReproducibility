
## G-Mixup: Graph Data Augmentation for Graph Classification
Xiaotian Han, Zhimeng Jiang, Ninghao Liu, Xia Hu
Keywords: 
Award: Outstanding Paper
ICML/2022/Proceedings/813 - G-Mixup: Graph Data Augmentation for Graph Classification.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the introduction (https://github.com/ahxt/g-mixup). In the readme they describe the work, how to install, how the data is fetched andopen questions. Code has okay comments. Structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(5/5)

Datasets are downloaded automatically in the implementation. The authors use REDDIT-BINARY, REDDIT-MULTI-5K, REDDIT-MULTI-12K, IMDB-BINARY and IMDB-MULTI. No other details given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

HP λ is defined in 3.1. and α in algorithm 2. Delta is varied between two settings. More hyperparameter values are stated in F.1, and a full structured overview is found in the implementation. No acquisition specified for all. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the experiment settings in appendix F, where htey state the data split, the selected split for the results, the metric (accuracy) and the population (10 runs) and aggregation is implied (average over the entire population). Variation is standard deviation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on geometrical deep learning.
