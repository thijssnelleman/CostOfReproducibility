
## Learning Auxiliary Monocular Contexts Helps Monocular 3D Object Detection
Xianpeng Liu, Nan Xue, Tianfu Wu
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/20074 - Learning Auxiliary Monocular Contexts Helps Monocular 3D Object Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/Xianpeng919/MonoCon). The readme contains an introduction on the method with examples, extensive installation instructions, data download and preparation instructions, training and evaluation/inference instructions, and a table with reproductions of their own model and the found values per reproductions + download link. The code seems well commented but the repository is rather large, and they seem to include many other repositories in their own. An index would be welcome to guide readers through the (directory) structure of the project.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a benchmark data set called KITTI, provide citations on it and key statistics + small description of the task. The authors provide a download link to it on the implementation docs.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Various hyperparameter values are stated in the paper and can easily be compared against the values in the implementation docs as they keep all configurations in seperate files. The authors do not specify an acquisition strategy for their values, but do present a short (modular) ablation study on their method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used, but it lacks a full explanation meaning the expertise required in this subfield is higher or this will require more research to set up a similar experiment. The authors state the training/validation set and that they use the benchmarks official test set evaluation on their server. This set up indicates a single model evaluation.  Training procedure is specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a thorough understanding of the 3D object detection task. This is not for a lack of documentation, rather the implementation documentation provides the independent investigators with loads of examples to understand the method, rather it is a complex method and task to grasp.
