
## CostFormer:Cost Transformer for Cost Aggregation in Multi-view Stereo
Weitao Chen, Hongbin Xu, Zhipeng Zhou, Yang Liu, Baigui Sun, Wenxiong Kang, Xuansong Xie
Keywords: Computer Vision: CV: 3D computer vision
IJCAI/2023/Proceedings/0067 - CostFormer:Cost Transformer for Cost Aggregation in Multi-view Stereo.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not share their implementation. In section 3.4 they share some details in 'common training settings' regarding the library used (with citation). In figure 2 they provide a detailed structure schematic on their method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors state in 4.3 the 5 public datasets they use for evaluations with citations, followed by short descriptions on each including statistics. No direct links are provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state the architecture parameters of their method in 3.4. The loss function is also stated. However a full overview on the hyperparameters is not given and many values seem to be mising. No specification on acquisition strategy on the given parameter values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are stated in the tables as F-score, where for each the mean is presented and per class. In the other results they use accuracy. Some metrics are a bit unclear, but do seem straight forward. The authors state static training/tests splits in 4.3. The results are single run/model. The training procedure is specified in 3.4.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a good understanding of CV, especially since the implementation has to be redone it also requires a lot of pratical experience.
