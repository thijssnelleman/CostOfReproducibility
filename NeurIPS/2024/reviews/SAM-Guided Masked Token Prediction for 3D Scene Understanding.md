
## SAM-Guided Masked Token Prediction for 3D Scene Understanding
Zhimin Chen, Liang Yang, Yingwei Li, Longlong Jing, Bing Li
Keywords: 
NeurIPS/2024/Proceedings/95998 - SAM-Guided Masked Token Prediction for 3D Scene Understanding.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state in the checklist they will release the code upon acceptance. This was not done. In figure 1 they illustrate the problem, in figure 2 the give an high level overview of the framework.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use ScanNet (citation) for pretraining and describe it. SUN RGB-D and S3DIS are also cited and used for evaluation but not described. No direct links given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyerparameter values in sec 4.1 but do not give a full overview. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use the official training/validation split of scannet, for the others this is not specified. The metrics used are average precision over thresholds, and mean accuracy and mean iou (all standard). The results are single run/model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on 3D cv and understanding. Since there is no implementation, practical experience as well.
