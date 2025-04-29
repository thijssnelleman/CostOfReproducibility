
## Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning
Shentong Mo, Peter Tong
Keywords: 
NeurIPS/2024/Proceedings/95692 - Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Pseudo code is available in C.2. The authors state in the checklist that the code is available as supplemental material. This can not be found in the paper or linked, nor on the NeurIPS poster page, openreview or the papers publication/proceedings page. Implementation is described in 4.1 but no practical details are given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(5/5)

The authors state the datasets used in 4.1. where they introduce ImageNet-1K (with citation) MS-COCO (with citation), ADE20K (Citation), DAVIS-2017 (citation in appendix C), Clevr (Citation). No direct links, descriptions or statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Hyperparameters are informally stated in 4.1, but an overview is missing. Acquisition is following the setup from another paper, but its not clear if this applies to all the parameter values. It is implied that the values are used for all experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors explain the evaluation metrics in 4.1. The data plit is given in 4.1 for Davis, for the others its not specified. The results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise in self supervised learning and contrastive learning.
