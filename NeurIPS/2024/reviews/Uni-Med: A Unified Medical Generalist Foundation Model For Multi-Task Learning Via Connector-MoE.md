
## Uni-Med: A Unified Medical Generalist Foundation Model For Multi-Task Learning Via Connector-MoE
Xun Zhu, Ying Hu, Fanbin Mo, Miao Li, Ji Wu
Keywords: 
NeurIPS/2024/Proceedings/93590 - Uni-Med: A Unified Medical Generalist Foundation Model For Multi-Task Learning Via Connector-MoE.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link for their implementation (https://github.com/MSIIP/Uni-Med). In the readme they state the method, how to install, how to download the data with direct links, and also pretrained models, how to set up the config file, how to run the code for training and evaluation for various examples. The code can use more comments. Structure is large and without index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors describe the datasets used in 4.1. The authors state two text only data sets (Medqa and pubmedqa with citations) image text pairs (Path-vqa and slake-vqa with citations) and RG (MPx-Single with cit) and CLS (Medmnist v2 with citation). The datasets are described in great detail in B.1. All datasets are linked in the implementation. No statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide a file with the configuration in the implementation. They are discussed in the implementation details paragraph of 4.1. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The data set splits are given in B.1. for training and testing. The authors report mean and standard deviations over 300k iterations. The evaluation metrics are stated in 4.1 with formulas and citations and extended in D.1. In the checklist they state the aggregation and deviation is calculated over three random seeds (runs).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requried expertise on foundation models, multi task learning and connector mixture of experts.
