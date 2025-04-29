
## PowerBEV: A Powerful Yet Lightweight Framework for Instance Prediction in Bird’s-Eye View
Peizheng Li, Shuxiao Ding, Xieyuanli Chen, Niklas Hanselmann, Marius Cordts, Juergen Gall
Keywords: Computer Vision: CV: Motion and tracking, Computer Vision: CV: Segmentation
IJCAI/2023/Proceedings/0120 - PowerBEV: A Powerful Yet Lightweight Framework for Instance Prediction in Bird’s-Eye View.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share their implementation online (https://github.com/EdwardLeeLPZ/PowerBEV). In the paper they provide detailed overviews of their method. The readme of the implementation has an index, updates, how to setup, where to download an place the datasets, where to find the pretrained models, instructions on training and how to change the configuration, how to run evaluation and visualise it. The code has a decent amount of comments/explanations. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors present direct download links in the implementation docs. In 4.,1. they state they use NuScenes dataset with citations, short description and some key statistics. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state several hyperparameters and training details in the implementation details section. However no details are mentioned regarding the acquisition of these values. The full configuration can be found in the implementation files.  The authors do a architecture ablation study in table 2 and 4.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state a fixed t/v/t split for the dataset in 4.1. The authors state their metrics with a full explanation in the 4.1 metrics paragraph. The results show single model/run values for the metrics.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries an understanding of CV due to the complexity of the problem/solution. The documentation is very complete, lowering the need for external documentation (experience). 
