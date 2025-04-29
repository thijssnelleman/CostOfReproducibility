
## Bifrost: 3D-Aware Image Compositing with Language Instructions
Lingxiao Li, Kaixiong Gong, Wei-Hong Li, xili dai, Tao Chen, Xiaojun Yuan, Xiangyu Yue
Keywords: 
NeurIPS/2024/Proceedings/94882 - Bifrost: 3D-Aware Image Compositing with Language Instructions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/lingxiao-li/Bifrost). In the readme they introduce the method with an illustration, provide updates, installation instructions, how to infer from the method, how to create dataset from the source data set (which they link), where to download pretrained models/weights, how to start training and acknowledgements of other code bases they used for theirs. The code has few comments, the repository structure is large and does not have an overview.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide a download link in the implementation for the COCO dataset. The authors state the dataset generation strategy in 3.1. and how they apply it to the COCO dataset (citation given). High level statistics are given in 3.1. on the new dataset. More detailed statistics in figure 12. Description is clear. Code for generation from COCO is provided. Data set statistics given in table 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are specified in 4.1 (Implementation details), more details in appendix A. No acquisition specified. An overview is given in the code, albeit hardcoded.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the evaluation results in table 2 (MSE and IoU) over various tasks. The results are single model. Evaluated on the test set, which is static (3.1, 4.1). The authors also conduct a user study which they detail in appendix F with how the users were presented with input (fig. 20), what data they collected and how it should be annotated and the population size. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in 3D CV and NLP crossover.
