
## SemanticMask: A Contrastive View Design for Anomaly Detection in Tabular Data
Shuting Tao, Tongtian Zhu, Hongwei Wang, Xiangming Meng
Keywords: Data Mining: DM: Anomaly/outlier detection, Machine Learning: ML: Unsupervised learning
IJCAI/2024/Proceedings/0262 - SemanticMask: A Contrastive View Design for Anomaly Detection in Tabular Data.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a source for their implementation (https://github.com/TST826/SemanticMask). In the readme they provide installation instructions, details on the data and where to find some analysis/features, an explanation of the code/repo structure, where to find their pretrained models and a short summary on the results. The code does not have a lot of comments, which does make it somewhat more effort to understand the flow of the process. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(9/9)

The authors provide details on the data and the files in the implementation docs. The authors state the datasets used in section 6.1 with citations. The authors state in the implementation additional details on the data can be found in the appendix but this is not found. The independent investigators will have to make an effort to get the details on each data set, as well as find the missing files for the other 8 but an example is given. It is implied by the authors that the data is public.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the values of their hyperparameters in section 6.1, and one is selected from a grid. The other values are not stated how they were determined. There is no summary of the HPs in the implementation, so to check all the values some effort is required.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they repeat each expriment five times and report the mean and std dev of the results. They state the metrics used with citation, which are common metrics although do require a base level of expertise in AI/ML to understand. The authors state the training is done with a 50-25-25 data split, which is randomised. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries a base understanding of ML techniques to follow the experiment, the method itself has a few layers to it of various ML techniques which do require some previous experience with NLP.
