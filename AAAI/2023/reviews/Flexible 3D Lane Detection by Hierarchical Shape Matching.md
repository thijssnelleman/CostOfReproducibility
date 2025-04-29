
## Flexible 3D Lane Detection by Hierarchical Shape Matching
Zhihao Guan, Ruixin Liu, Zejian Yuan, Ao Liu, Kun Tang, Tong Zhou, Erlong Li, Chao Zheng, Shuqi Mei
Keywords: CV: Object Detection & Categorization, CV: Vision for Robotics & Autonomous Driving, CV: Scene Analysis & Understanding, CV: Applications
AAAI/2023/Proceedings/25146 - Flexible 3D Lane Detection by Hierarchical Shape Matching.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide a link to their repository (https://github.com/Doo-do/FHLD). Here they provide an architecture and some examples. There is some code available but there is not a lot of documentation/comments on it. In the readme the authors state they 'are busy reviewing our codes recently, and will release the codes ASAP (no later than summer holiday)'. It is unclear what of the code is currently relevant because of this comment. Reverse engineering with a critical eye required. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(0/2)

The authors use two data sets: A public data set which they annotated themselves, and a data set they completely collected themselves. They provide clear details on the data set. They do not seem to release the data (nor the self labelled public one). They state there are no readily available large scale public data sets with 3D lane annotations, so independent investigators would probably have to acquire one from scratch.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are given in the details section of the experiments section. They can be easily checked in the implementation where they are collected in a single file. No details given on how these values were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors discuss and motivate the metrics used. They staate the data sets are randomly split 80/20 for training and testing. The results seem to indicate single runs, however they do state "three parallel experiments are carried out for each method" but no aggregation is stated. This can perhaps be verified in the implementation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a good understanding of object detection and point clouds. Especially if the data will have to be collected or constructed by the independent investigators themselves.
