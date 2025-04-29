
## Attention-Based Depth Distillation with 3D-Aware Positional Encoding for Monocular 3D Object Detection
Zizhang Wu, Yunzhe Wu, Jian Pu, Xianzhi Li, Xiaoquan Wang
Keywords: CV: 3D Computer Vision, CV: Applications
AAAI/2023/Proceedings/25391 - Attention-Based Depth Distillation with 3D-Aware Positional Encoding for Monocular 3D Object Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors published their code (https://github.com/rockywind/ADD). However, the repository only contains the MIT license. Some implementation details are given in the paper, but these are mainly hyperparameter values. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors evaluate their method on a public benchmark dataset (KITTI) and cite the source.  There is a short description on the data set. There is no reference to the data in the implementation documentation because its empty.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The hyperparameter values are given in the implementation details. However, as the actual implementation is empty its ahrd to check if all HP values are given that we need or that some less 'important' values have been forgotten. No details are given regarding the acquisition of the configuration.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors specify the speration of training/validation and test split and cite a previous work as motivation. The evaluation metrics are well documented. It can be inferred from the paper that the results are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The metrhod requires a good understanding on computer vision.
