
## Unsupervised Voice-Face Representation Learning by Cross-Modal Prototype Contrast
Boqing Zhu, Kele Xu, Changjian Wang, Zheng Qin, Tao Sun, Huaimin Wang, Yuxing Peng
Keywords: Machine Learning: Multi-modal learning, Computer Vision: Biometrics, Face, Gesture and Pose Recognition, Machine Learning: Self-supervised Learning, Machine Learning: Unsupervised Learning
IJCAI/2022/Proceedings/0526 - Unsupervised Voice-Face Representation Learning by Cross-Modal Prototype Contrast.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/Cocoxili/CMPC). In the readme they introduce the method with an illustration, state the installation requirements, where to download the pretrained models, how to pre-process the data, how to train and to evaluate the method. They also state what data can be found where in the repository. The code has some comments but a lot of it is undocumented leaving a lot to be reverse engineered. The authors provide an overview of the method on a high level in figure 2. The authors specify implementation details in 5.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors state the data set they use in 4.1, provide a description and some statistics and citations. The data can be found in the implementation, as stated at the end of 4.1. The preprocessing code is available, and explained in 5.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in 5.1. The authors summarise the full configurations and parameters in the implementation docs. The authors do not specify an acquisition strategy or budget.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state how the data is split in training and test data in 4.1, with a reference to a previous work for motivation. In section 5 they state the evaluation protocol and what metrics are being reported, most of which are standard (task specific but the metrics itself are not complicated). Based on the given data splits, its easy to recognise all results are single run/model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries experience in selfsupervised/unsupervised learning, CV and the task (voice-face combination).
