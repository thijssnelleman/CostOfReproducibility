
## SpFormer: Spatio-Temporal Modeling for Scanpaths with Transformer
Wenqi Zhong, Linzhi Yu, Chen Xia, Junwei Han, Dingwen Zhang
Keywords: CV: Applications, CV: Representation Learning for Vision
AAAI/2024/Proceedings/29153 - SpFormer: Spatio-Temporal Modeling for Scanpaths with Transformer.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4] 

The authors provide a source code repository (https://github.com/wenqizhong/SpFormer). The readme is empty however, and comments are extremely sparse. The authors provide an extensive illustration in their paper on the architecture. To understand what happens in the implementation could be relatively difficult.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/4)

The authors provide results on three tasks: ASD, toddler age predicition and visual perceptual task prediction.
    - The first has two datasets, one publicly available and cited and one collected by the authors does not have a publication provided. Both have metrics provided on them.
    - The second task has one data set, publicly available, with citation and meta data reported.
    - Third has one publicly available dataset with citation and statistics

The private data set would be benficial to also publish, but enough information was provided for comparison sake.


### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide an ablation study on two hyperparameters with grid search. Other hyperparameters and values are not specified nor their acquisition budget, but the values could be extracted from the implementation. This would take some work due to the lack of documentation on the implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors in general state the task quite clearly, or reference the experimental protocol introduced on these tasks in previous works. The implementation docs could also be used, albeit more complex to extract it from here. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The authors introduce a new model for spatio temporal modeling, and requires some expertise on this data type, as well as transformers. The method is well documented with examples and reviewed on many tasks. The source code could help even more with lowering this threshold by being well documented, as it can reduce the entry level to experiment with the presented work.
