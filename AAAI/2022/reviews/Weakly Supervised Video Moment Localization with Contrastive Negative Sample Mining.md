
## Weakly Supervised Video Moment Localization with Contrastive Negative Sample Mining
Minghang Zheng, Yanjie Huang, Qingchao Chen, Yang Liu
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/20263 - Weakly Supervised Video Moment Localization with Contrastive Negative Sample Mining.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/minghangz/cnm). Their readme contains an introduction, a visualisation of the framework/pipeline, tables with results and links to the models, requirements for the code to work (versions missing, can be reverse engineered), data download/preparation/structure explanation, training instructions per data set and inference instructions. They use configuration files to specify the model architecture / hyperparameters, and the code has good comments. Details on the data preprocessing and the model settings are also given in the implementation details section.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two publicly available data sets, provide citations on them, a description, statistics and direct download links in the implementation repository. Data loaders / preprocessors are available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors fully specify the hyperparameter values in the implementation documentation and some are explained in the paper (model settings section). No details are given on how the configuration was acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state their evaluation metric and provide citations on it. They state they use a static train test split as provided by the data source. They present single model results (implied, could have been stated explicitly) and everything can easily be checked with their implementation docs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The documentation on the method is extensive, making the method easier to follow and requiring less reliance on external documentation. However, it does still require a good understanding on computer vision in general and the presented task as it is a complex framework.
