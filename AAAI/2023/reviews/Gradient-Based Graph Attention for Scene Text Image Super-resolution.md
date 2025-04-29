
## Gradient-Based Graph Attention for Scene Text Image Super-resolution
Xiangyuan Zhu, Kehua Guo, Hui Fang, Rui Ding, Zheng Wu, Gerald Schaefer
Keywords: CV: Low Level & Physics-Based Vision, CV: Image and Video Retrieval, CV: Interpretability and Transparency, CV: Language and Vision, CV: Learning & Optimization for CV, CV: Applications
AAAI/2023/Proceedings/25499 - Gradient-Based Graph Attention for Scene Text Image Super-resolution.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation link (https://github.com/xyzhu1/TSAN). There the authors state the requirements needed for the code, a link to download the dataset resources and where to place them in the directory structure. A short description on how to do the testing is give, the training section is described as 'coming'. A link to a pretrained model with a password is also provided, albeit with little context. The configuration is provided as a seperate yaml file. The code has some comments but could use more. The directory structure is rather large and could do with an index/explanation. An architecture overview is given in the paper. A short summary of implementation details are given. If the details in the repository (e.g. readme + comments) were improved, this cost should be 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide download links in their implementation repository. They provide a citation on it in their paper and a description with detailed statistics. They also state how they divide the data into training and testing data. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide a configuration yaml file in their implementation making it very clear which (default) values are used. These details are also (partially) stated in the implementation details. The authors also provide an ablation study on the modules in their method. It is not specified how the hyperparameter values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state which metrics they use to evaluate, but provide little details on them. From the results its made clear they are single run results. Details regarding training procedures are given and can be relatively easily verified with the implementation documentation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method goes deep into computer vision applications regarding text recognition and super resolution data. Some examples are given and the implementation helps as supplementary documentation.
