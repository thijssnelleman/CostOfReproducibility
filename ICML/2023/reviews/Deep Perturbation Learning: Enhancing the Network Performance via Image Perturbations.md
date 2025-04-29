
## Deep Perturbation Learning: Enhancing the Network Performance via Image Perturbations
Zifan Song, Xiao Gong, Guosheng Hu, Cairong Zhao
Keywords: 
ICML/2023/Proceedings/23945 - Deep Perturbation Learning: Enhancing the Network Performance via Image Perturbations.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide pseudo code on their method in algorithm 1/2. The authors state they use PyTorch to implement their method in section 4.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors use six benchmark datasets from three vision tasks. They provide citations and statistical summaries on them in appendix C. No direct links or descriptions igven.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors summarise the hyperparameter values in section 4.1. They measure the effect of HP alpha on a grid in table 5 on the test set. In figure 2b they experiment with HP epsilon of their method. There is not a full hyperparameter value acquisition explanation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use top-1 accuracy, mean average precision, COCO (which they state is standard), mIoU (mean intersection over union) and loss. The results are single model. The test sets are given per dataset in appendix C.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experinece with pertubation in image tasks and CV.
