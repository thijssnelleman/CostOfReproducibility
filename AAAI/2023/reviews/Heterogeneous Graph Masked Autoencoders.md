
## Heterogeneous Graph Masked Autoencoders
Yijun Tian, Kaiwen Dong, Chunhui Zhang, Chuxu Zhang, Nitesh V. Chawla
Keywords: ML: Graph-based Machine Learning, DMKM: Graph Mining, Social Network Analysis & Community Mining, ML: Unsupervised & Self-Supervised Learning, ML: Deep Generative Models & Autoencoders
AAAI/2023/Proceedings/26192 - Heterogeneous Graph Masked Autoencoders.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/meettyj/HGMAE). In the readme they briefly state how to run the code and what data sets / tasks are supported. They have a detailed config.yml file with configurations provided per data set. There are comments in the code but some important files could use more of them. The readme could be a bit more detailed as well. However, as it is a small repository, the impact is much less. A large framework schematic is provided in the paper. Implementation details are noted in the experiments section.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

Data sets and loaders are provided in the implementation. The paper discussed the four data sets and provides citations on them. Statistics/details on the datasets and their tasks are not specified, but could be extracted from the citations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors denote two hyperparameters on their method. They describe the values of these and a few other HPs in the experiments section. Exact values of each can easily be retrieved from the implementation documentation. No specifications are given on how these values were determined.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state they report the mean and std for 10 runs with random seeds, and the training/validation/testing splits on the data is given. They briefly note the metrics used for evaluation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method is from the geometrical deep learnming domain, and deals with auto encoders. There is some knowledge requires on graph neural networks to completely follow the method and its mathematics.
