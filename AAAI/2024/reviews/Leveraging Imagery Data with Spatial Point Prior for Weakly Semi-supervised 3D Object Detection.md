
## Leveraging Imagery Data with Spatial Point Prior for Weakly Semi-supervised 3D Object Detection
Hongzhi Gao, Zheng Chen, Zehui Chen, Lin Chen, Jiaming Liu, Shanghang Zhang, Feng Zhao
Keywords: CV: Object Detection & Categorization, CV: Multi-modal Vision, CV: Vision for Robotics & Autonomous Driving, ROB: Multimodal Perception & Sensor Fusion
AAAI/2024/Proceedings/27916 - Leveraging Imagery Data with Spatial Point Prior for Weakly Semi-supervised 3D Object Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]
The authors state that their implementation was build using a toolkit called MMDetection3D toolkit, but it is not specified whether this toolkit is open source or not. No link to their source code is given, nor is a citation/link for the toolkit given. The authors do clearly document their method with many visualizations and mathematical expressions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors give a clear description on the used data set, regarding features and population size, it is publicly available and they state it is widely used.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

There seems to be no explanation of the configurable parameters of the method, values of the algorithm configuration or hyperparameters, nor under which budget these were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors clearly explain the evaluation metrics used for their experimental procedure, and also reason why deviations of their own metric (SPNDS) is relevant. However, it is not clearly specified how the 2%, 5% and 10% sampling is done and how frequently the experiment was repeated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The work is clearly deeply invested within the 3D object detection field, and leverages many prior techniques the independent investigators would need to understand in order to reproduce the method. However, due to the clear documentation on their own method and the substantial amount of citations that can be used, the road towards understanding the paper should be rather straightforward.
