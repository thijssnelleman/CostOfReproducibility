
## X-RefSeg3D: Enhancing Referring 3D Instance Segmentation via Structured Cross-Modal Graph Neural Networks
Zhipeng Qian, Yiwei Ma, Jiayi Ji, Xiaoshuai Sun
Keywords: CV: 3D Computer Vision, CV: Language and Vision
AAAI/2024/Proceedings/28501 - X-RefSeg3D: Enhancing Referring 3D Instance Segmentation via Structured Cross-Modal Graph Neural Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide an implementation source of their method (https://github.com/qzp2018/X-RefSeg3D). The readme documents requirements, how to download the data sets, a small index on how the data is structured, how to preprocess the data, explanations on how to fetch and place the pretrained models, and finally how to train and validate the model. They also provide acknowledgements on where modified code is sourced from. They do not provide comments on their code in great abundance. The structure is relatively small, making it easier to oversee. The authors provide illustrations on their framework in the paper, including a large overview. They also provide and implementations details section with more specifications.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use two data sets, provide statistics on them but a citation is not found. Instructions on how to acquire them are given in the implementation documentation, complete with processing instructions.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide hyperparmater values and semantic parameters in the implementation details section. Some values could be missing, but can with a bit of effort extracted from the implementation. However there is no explanation how these values were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors provide details on training and the metrics used. Their implementation details seem to suggest singular results, but this would need some verification.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

According to the authors this is the second work regarding 3D instance segmentation. They provide an extensive introduction to the topic with several examples. Thus some experience with (3D) computer vision can be required, the set up of the paper lowers this cost and the inclusion of the implementation provides a clear example on the method as well.
