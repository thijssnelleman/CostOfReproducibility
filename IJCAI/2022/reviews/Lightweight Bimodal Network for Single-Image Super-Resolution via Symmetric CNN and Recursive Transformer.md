
## Lightweight Bimodal Network for Single-Image Super-Resolution via Symmetric CNN and Recursive Transformer
Guangwei Gao, Zhengxue Wang, Juncheng Li, Wenjie Li, Yi Yu, Tieyong Zeng
Keywords: Computer Vision: Machine Learning for Vision, Computer Vision: Computational photography, Computer Vision: Representation Learning, Machine Learning: Feature Extraction, Selection and Dimensionality Reduction
IJCAI/2022/Proceedings/0128 - Lightweight Bimodal Network for Single-Image Super-Resolution via Symmetric CNN and Recursive Transformer.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state a link to their implementation (https://github.com/IVIPLab/LBNet). In the readme they state the dependencies, where to download the datasets, results and pretrained model links, how to evaluate, examples of how to run the training procedure, how to test, results from the paper, and acknowledgements of used frameworks/repositories. A lot of the code is without comments. An illustration on the architecture is given in figure 2 and 3. In 4.2 some details are stated.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors state the datasets used (one for training and five benchmark datasets to test) with citations. The datasets are not described nor are statistics given. Direct download links are given in the implementation docs. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state various hyperparmaeters in 4.2, and all options for the method are summarised in the implementation docs in a single file with default values. They use two configuration/architectures in the paper and outline the differences in 4.2. However a full configuration file is not given, so the default parameter values in the option file will have to be assumed in case values are not stated in the paper. No acquistion method stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the metrics in section 4.1, but they are not explained. The results are single run. The test data sets are stated in 4.1. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in Computer Vision to understand the task/evaluation and transformer models.
