
## CLE-ViT: Contrastive Learning Encoded Transformer for Ultra-Fine-Grained Visual Categorization
Xiaohan Yu, Jun Wang, Yongsheng Gao
Keywords: Machine Learning: ML: Classification, Machine Learning: ML: Applications
IJCAI/2023/Proceedings/0504 - CLE-ViT: Contrastive Learning Encoded Transformer for Ultra-Fine-Grained Visual Categorization.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/Markin-Wang/CLEViT). The authors introduce the method with a visualisation, provide installation instructions, how to install, where to download the pretrained models, where to download the datasets with a link, how to run the training scripts, and how to download the trained models. The repository directory/file structure is large but the code has a decent amount of comments. The authors provide implementation details in 4.2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(7/7)

The authors provide direct two download links to 6 datasets in their implementation docs. The apple data set is not directly linked, but the citation implies its public. They state details on them with citation on a few in 4.1 and provide statistics on them in table 1. Most of the datasets seem to be possible for download from the provided links but this would have to be checked. Basically the information is almost complete but with a few more descriptions this would have been a 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the parameter values per data set in 4.2. The missing values can be found in the implementation docs. There is no statement on how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the training procedure in 4.2, the metrics used in 4.3 (and the caption of the tables). Train/dev/test data splits can be found in the implementation and they are summarised in table 1. However it is not clearly stated how it is exactly evaluated, which will have to be checked.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience in transformers.
