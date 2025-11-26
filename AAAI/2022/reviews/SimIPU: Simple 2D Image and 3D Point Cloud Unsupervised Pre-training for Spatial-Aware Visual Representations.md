
## SimIPU: Simple 2D Image and 3D Point Cloud Unsupervised Pre-training for Spatial-Aware Visual Representations
Zhenyu Li, Zehui Chen, Ang Li, Liangji Fang, Qinhong Jiang, Xianming Liu, Junjun Jiang, Bolei Zhou, Hang Zhao
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/20040 - SimIPU: Simple 2D Image and 3D Point Cloud Unsupervised Pre-training for Spatial-Aware Visual Representations.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a source for their implementation. Overview in figure 1/2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use two open data sets, provide statics on them and citations and choices on how they use it for their experiment. A direct link is missing, as well as a description on the data/task.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors define two hyperparameters on their loss function (loss weights). A single parameter (temperature factor) value is given regarding contrastive learning. No other values given.


### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state how they use the data for the experiment. The test set is given static, defining how it is applied in the experiment. The results seem to be single model. The metrics are not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method requires a good understanding of point cloud and computer vision, as many details are ommitted as expected experience of the reader. 
