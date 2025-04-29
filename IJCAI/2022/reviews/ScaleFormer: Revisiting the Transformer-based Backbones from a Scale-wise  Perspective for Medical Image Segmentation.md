
## ScaleFormer: Revisiting the Transformer-based Backbones from a Scale-wise Perspective for Medical Image Segmentation
Huimin Huang, Shiao Xie, Lanfen Lin, Yutaro Iwamoto, Xian-Hua Han, Yen-Wei Chen, Ruofeng Tong
Keywords: Computer Vision: Segmentation, Computer Vision: Biomedical Image Analysis
IJCAI/2022/Proceedings/0135 - ScaleFormer: Revisiting the Transformer-based Backbones from a Scale-wise Perspective for Medical Image Segmentation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/ZJUGiveLab/ScaleFormer). In the readme they state the datasets used with direct links and acquisition instructions for two, one is stated to 'be uploaded later' (3 years ago, checked on 18-03-2025), they provide environment/dependency details for installation and a list of reference repositories. The code has some comments but many of them are a bit cryptic. There is a list of instances used for training and testing and a dataloader. The repository seems to be missing an entrypoint/instructions on how to run. However, this will still serve as a good starting point for independent investigators to work with. The paper provides illustrations/overview/comparison architectures on the method in figures 3, 4 and 5. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors state the datasets used in the implementation docs, with direct links / acquisition instructions for two of them. The authors state descriptions, key statistics and citations on all of them in 4.1. They all seem to be publicly available (allbeit on request), including the one missing in the implementation docs. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values used for each dataset experiment in section 4.2. There is no HP/search space defined, but this can easily be extracted from the implementation. The architecture values seem to be hardcoded into the implementation. There is no acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors sate the train/test split for two datasets (static/provided) and how they generated it for the third. Thery present the results with various subfield specific metrics (and classes) in table 1, they explain the meating of the metrics in the dataset/task description, which are either standard or standard for the subfield (slightly raising the expertise). The results are single model/run (static test set, no variance or aggregation specified regarding seeding).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on the medical subfield/problem, transformers and CV.
