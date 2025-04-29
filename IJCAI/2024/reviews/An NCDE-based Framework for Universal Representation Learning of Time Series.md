
## An NCDE-based Framework for Universal Representation Learning of Time Series
Zihan Liu, Bowen Du, Junchen Ye, Xianqing Wen, Leilei Sun
Keywords: Machine Learning: ML: Representation learning, Machine Learning: ML: Self-supervised Learning, Machine Learning: ML: Time series and data streams
IJCAI/2024/Proceedings/0511 - An NCDE-based Framework for Universal Representation Learning of Time Series.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/LiuZH-19/CTRL). In the readme the authors state the requirements and how to install, how the data sets can be obtained with direct links and how to place in them in the directory structure, how to run the training script and an extensive explanation of each hyperparameter, and where the results can be found. The code has a decent amount of comments and explanations, but could do with some more. The directory structure / number of files to browse is not small, but still overseeable. In general the implementation is well documented. The authors provide a large architecture overview (figure 2).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(32/32)

The authors provide direct download links to the data in their implementation documentation. In the paper they provide either citations or direct links on the data used. A short description on each dataset is given. Some statistics on the data would be welcome, however they can be easily determined using the presented links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors dedicate a section regarding reproduction details of their method, which includes details regarding the hyperparameter settings. The details are seemingly complete an can easily be checked with the implementation docs. The authors state some parameters are tuned on a grid or range, the others are set emperically. The authors have included detailed settings for each experiment in our public code. They also do a modular ablation study.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state they repeat each experiment with random seeds five times an present averaged metrics. The authors state the used evaluation metrics, without explanation but it is a common/standard metric. No clear details are given regarding train/validation/test splits, but could be derived from the given data sources and implementation documentation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method requires a good understanding on time series data. The authors present a unified framework on it.
