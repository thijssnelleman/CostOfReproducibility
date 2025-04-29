
## Assessing a Single Image in Reference-Guided Image Synthesis
Jiayi Guo, Chaoqun Du, Jiangshan Wang, Huijuan Huang, Pengfei Wan, Gao Huang
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/19956 - Assessing a Single Image in Reference-Guided Image Synthesis.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state their method is implemented in PyTorch. A schematic on their method/pipeline is given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(5/5)

The authors use five datasets in their work, provide citations on them, and a short application description. However, no statistics or descriptions on the data are given. Direct links are absent possibly due to no implementation documentation. It is implied in the text that the datasets are public, but a clear statement on this would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide hyperparameter details per model. Its difficult to verify that these are all needed values, however the section seems quite extensive. No acquisition strategy is specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors refer for the training procedure to previous work, document their human evaluation extensively, and how the sampling was done. The metrics are briefly described and cited. However, due to the complexity of the experiments, this might still be a some work to set up (not for the lack of documentation persay).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires a good understanding on the task / generative AI on computer vision.
