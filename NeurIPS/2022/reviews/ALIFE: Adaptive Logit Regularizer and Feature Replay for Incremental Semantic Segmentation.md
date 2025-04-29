
## ALIFE: Adaptive Logit Regularizer and Feature Replay for Incremental Semantic Segmentation
Youngmin Oh, Donghyeon Baek, Bumsub Ham
Keywords: 
NeurIPS/2022/Proceedings/54768 - ALIFE: Adaptive Logit Regularizer and Feature Replay for Incremental Semantic Segmentation.pdf
Project URL: https://cvlab.yonsei.ac.kr/projects/ALIFE/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their project page in the subtitle, where they link the implementation (https://github.com/cvlab-yonsei/ALIFE). In the readme they state installation instructions, how the dataset structure should be organised, how to run training scripts and other repositories they build upon. Code has okay comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

Datasets used are ADE20K and PASCAL VOC (citations provided). No details provided otherwise.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameter values in appendix B and state some are acquired empirically, some with grid search (grids provided), some are 'default' and that corss-validation is done to select them. The selected values are summarised in table B. There are also files available regarding configurations per experiment. For most acquisition is clear but not for all.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metric is IoU. Data split is static (stated in 4.1.). Results are reported over 3 runs with different seeds and averaged. They report the results on the validation set. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on semantic segmantation.
