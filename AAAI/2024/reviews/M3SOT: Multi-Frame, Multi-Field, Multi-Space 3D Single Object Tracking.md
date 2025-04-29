
## M3SOT: Multi-Frame, Multi-Field, Multi-Space 3D Single Object Tracking
Jiaming Liu, Yue Wu, Maoguo Gong, Qiguang Miao, Wenping Ma, Cai Xu, Can Qin
Keywords: CV: 3D Computer Vision, CV: Motion & Tracking, CV: Vision for Robotics & Autonomous Driving
AAAI/2024/Proceedings/28306 - M3SOT: Multi-Frame, Multi-Field, Multi-Space 3D Single Object Tracking.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors provide an implementation source in the abstract (https://github.com/ywu0912/TeamCode.git). The readme is empty. The code also seems to be without any comments. It would thus require serious effort to understand the layout and flow of the process. The authors do provide three small illustrations and one large framework diagram on the work flow of their method which helps with understanding the implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use three datasets which they cite and are seemingly public as they state they are benchmark datasets. The authors seem to provide data processors in their implementation documentation, however it takes some effort to really understand how this works. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

There are no clear statements on hyperparameters in the paper. These values can possibly be extracted from the implementation, but this requires some serious work to verify whether its correct or not.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used for evaluation and cite their evaluation method used in the procedure, state the data split used for evaluation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method presents a complex architecture and on a non-straightforward data type for a clear task. The lack of documentation in the implementation will require serious effort when attempting reproduction of the presented method, but is not completely unwarranted as it is in general not an easy task to grasp.
