
## MagicPose: Realistic Human Poses and Facial Expressions Retargeting with Identity-aware Diffusion
Di Chang, Yichun Shi, Quankai Gao, Hongyi Xu, Jessica Fu, Guoxian Song, Qing Yan, Yizhe Zhu, Xiao Yang, Mohammad Soleymani
Keywords: 
ICML/2024/Proceedings/33301 - MagicPose: Realistic Human Poses and Facial Expressions Retargeting with Identity-aware Diffusion.pdf
Project URL: https://boese0601.github.io/magicdance/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/Boese0601/MagicDance). The authors state in the readme example output, download links to pretrained models and pre-processed dataset download links, how to place it in their implementation, how to install the required dependencies, how to run inference on the method including the test set, how to run training, how to use your own dataset for training, general information and an index on the code files, and acknowledgements for other repositories theirs build upon. The amount of comments in the code is varying a lot per file. The repository structure is very large and a proper index on this would help a lot understanding what can be found where. An overview on the method can be found in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/3)

The authors present a direct link to a dataset in their implementation and to various pretrained models. The authors state they processed this dataset and how in 5.1. They also provide citations, statistics and descriptions on this data. The second data set the authors cite, describe briefly but no statistics and no direct link. The third dataset seems private and very little details are given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state various hyperparameter values in 5.2. A full overview on the HP space is missing in the paper, but can be easily extracted from the implementation entry point. No acquisition method specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the metrics used in 5.3 with citation but no explanation except for their own novel metric which is fully specified. The results are single model. The training and testing sets are specified in 5.1. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in CV.
