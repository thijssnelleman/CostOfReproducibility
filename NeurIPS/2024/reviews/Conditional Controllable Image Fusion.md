
## Conditional Controllable Image Fusion
Bing Cao, Xingxin Xu, Pengfei Zhu, Qilong Wang, Qinghua Hu
Keywords: 
NeurIPS/2024/Proceedings/95168 - Conditional Controllable Image Fusion.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/jehovahxu/CCF). In the readme they introduce the method with abstract and figures, state how to install, where to download pretrained models and how to infer. The code has decent comments. There are quite a lot of files so an index is welcome. Implementation details are given in sec 5.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors state the datasets used (LLVIP, MFFW and MEFB) in section 5. with citations. No descriptions or statistics given nor direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

In section 4.3 θ is defined as a hyperparameter. In algorithm 1 no parameters are defined but there are some variables in the code. There are some configuration files in the implementation. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors consider three tasks (image fusion scenarios). For each task they use a seperate dataset. The metrics are stated in sec 5 where they define each with their acronym but they are not explained (not all are standard in general but for the subfield thus experience is required). The test sets are defined in sec 5 by citing previous works but not explicitly written. The authors evaluate single models in table 1 and 2.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in image fusion tasks 
